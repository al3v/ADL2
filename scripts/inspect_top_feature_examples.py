import argparse
import pandas as pd
import torch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--features-input", default="outputs/sae_features_switching_base_v2.pt")
    parser.add_argument("--metadata-input", default="reports/hidden_states_metadata_base_v2.csv")
    parser.add_argument("--diff-input", default="reports/sae_top_differential_features_base_v2.csv")
    parser.add_argument("--output", default="reports/sae_top_feature_examples_base_v2.md")
    parser.add_argument("--top-n-features", type=int, default=5)
    parser.add_argument("--top-n-examples", type=int, default=8)
    args = parser.parse_args()

    feature_rows = torch.load(args.features_input)
    meta = pd.read_csv(args.metadata_input)
    diff = pd.read_csv(args.diff_input)

    rows = []
    for r in feature_rows:
        rows.append({
            "fact_id": r["fact_id"],
            "variant_id": r["variant_id"],
            "layer": int(r["layer"]),
            "is_correct": bool(r["is_correct"]),
            "feature_acts": r["feature_acts"],
        })

    feats = pd.DataFrame(rows)

    merged = feats.merge(
        meta,
        on=["fact_id", "variant_id", "layer", "is_correct"],
        how="left",
    )

    with open(args.output, "w", encoding="utf-8") as f:
        f.write("# Top activating examples for differential SAE features\n\n")
        f.write("This report shows which prompts activate the most correct-associated and wrong-associated SAE features.\n\n")

        for layer in sorted(diff["layer"].unique()):
            f.write(f"## Layer {layer}\n\n")

            for direction in ["more_active_in_correct", "more_active_in_wrong"]:
                f.write(f"### {direction}\n\n")

                selected = diff[
                    (diff["layer"] == layer)
                    & (diff["direction"] == direction)
                ].head(args.top_n_features)

                for _, feat_row in selected.iterrows():
                    feature_idx = int(feat_row["feature_index"])
                    f.write(f"#### Feature {feature_idx}\n\n")
                    f.write(f"- Rank: {int(feat_row['rank'])}\n")
                    f.write(f"- Mean diff correct minus wrong: `{feat_row['mean_diff_correct_minus_wrong']:.4f}`\n")
                    f.write(f"- Correct mean activation: `{feat_row['correct_mean_activation']:.4f}`\n")
                    f.write(f"- Wrong mean activation: `{feat_row['wrong_mean_activation']:.4f}`\n\n")

                    example_rows = []

                    for _, r in merged[merged["layer"] == layer].iterrows():
                        act = r["feature_acts"][feature_idx].item()
                        example_rows.append({
                            "activation": act,
                            "fact_id": r["fact_id"],
                            "variant_id": r["variant_id"],
                            "is_correct": r["is_correct"],
                            "question": r["question"],
                            "correct_answer": r["correct_answer"],
                            "generated_answer": r["generated_answer"],
                        })

                    ex = pd.DataFrame(example_rows).sort_values("activation", ascending=False).head(args.top_n_examples)

                    f.write("| activation | fact_id | variant | correct | question | generated answer |\n")
                    f.write("|---:|---|---|---|---|---|\n")

                    for _, e in ex.iterrows():
                        question = str(e["question"]).replace("|", "\\|")
                        generated = str(e["generated_answer"]).replace("|", "\\|").replace("\n", " ")
                        f.write(
                            f"| {e['activation']:.4f} "
                            f"| {e['fact_id']} "
                            f"| {e['variant_id']} "
                            f"| {e['is_correct']} "
                            f"| {question} "
                            f"| {generated} |\n"
                        )

                    f.write("\n")

    print("Saved:", args.output)


if __name__ == "__main__":
    main()
