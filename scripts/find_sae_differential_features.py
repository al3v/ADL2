import argparse
import pandas as pd
import torch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="outputs/sae_features_switching_base_v2.pt")
    parser.add_argument("--output", default="reports/sae_top_differential_features_base_v2.csv")
    parser.add_argument("--top-k", type=int, default=50)
    args = parser.parse_args()

    rows = torch.load(args.input)

    records = []
    for r in rows:
        records.append({
            "fact_id": r["fact_id"],
            "variant_id": r["variant_id"],
            "layer": int(r["layer"]),
            "is_correct": bool(r["is_correct"]),
            "feature_acts": r["feature_acts"],
        })

    df = pd.DataFrame(records)
    out_rows = []

    for layer, group in df.groupby("layer"):
        correct = group[group["is_correct"] == True]
        wrong = group[group["is_correct"] == False]

        if len(correct) == 0 or len(wrong) == 0:
            continue

        correct_acts = torch.stack(correct["feature_acts"].tolist())
        wrong_acts = torch.stack(wrong["feature_acts"].tolist())

        correct_mean = correct_acts.mean(dim=0)
        wrong_mean = wrong_acts.mean(dim=0)

        correct_freq = (correct_acts > 0).float().mean(dim=0)
        wrong_freq = (wrong_acts > 0).float().mean(dim=0)

        mean_diff = correct_mean - wrong_mean
        freq_diff = correct_freq - wrong_freq

        top_correct_values, top_correct_idx = torch.topk(mean_diff, args.top_k)
        top_wrong_values, top_wrong_idx = torch.topk(-mean_diff, args.top_k)

        for rank, (idx, value) in enumerate(zip(top_correct_idx.tolist(), top_correct_values.tolist()), start=1):
            out_rows.append({
                "layer": layer,
                "direction": "more_active_in_correct",
                "rank": rank,
                "feature_index": idx,
                "mean_diff_correct_minus_wrong": value,
                "correct_mean_activation": correct_mean[idx].item(),
                "wrong_mean_activation": wrong_mean[idx].item(),
                "correct_activation_frequency": correct_freq[idx].item(),
                "wrong_activation_frequency": wrong_freq[idx].item(),
                "frequency_diff_correct_minus_wrong": freq_diff[idx].item(),
            })

        for rank, (idx, value) in enumerate(zip(top_wrong_idx.tolist(), top_wrong_values.tolist()), start=1):
            out_rows.append({
                "layer": layer,
                "direction": "more_active_in_wrong",
                "rank": rank,
                "feature_index": idx,
                "mean_diff_correct_minus_wrong": -value,
                "correct_mean_activation": correct_mean[idx].item(),
                "wrong_mean_activation": wrong_mean[idx].item(),
                "correct_activation_frequency": correct_freq[idx].item(),
                "wrong_activation_frequency": wrong_freq[idx].item(),
                "frequency_diff_correct_minus_wrong": freq_diff[idx].item(),
            })

    out = pd.DataFrame(out_rows)
    out.to_csv(args.output, index=False)

    print("Saved:", args.output)
    print("Rows:", len(out))
    print()
    print(out.head(20))


if __name__ == "__main__":
    main()
