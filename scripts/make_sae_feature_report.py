import argparse
import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="reports/sae_top_differential_features_base_v2.csv")
    parser.add_argument("--output", default="reports/sae_top_differential_features_base_v2.md")
    parser.add_argument("--top-n", type=int, default=10)
    args = parser.parse_args()

    df = pd.read_csv(args.input)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write("# SAE differential features for base Gemma switching facts\n\n")
        f.write("This report lists SAE features that are more active for correct vs wrong prompt variants of the same fact.\n\n")

        for layer in sorted(df["layer"].unique()):
            f.write(f"## Layer {layer}\n\n")

            for direction in ["more_active_in_correct", "more_active_in_wrong"]:
                f.write(f"### {direction}\n\n")

                sub = df[(df["layer"] == layer) & (df["direction"] == direction)].head(args.top_n)

                f.write("| rank | feature_index | mean_diff_correct_minus_wrong | correct_mean | wrong_mean | correct_freq | wrong_freq |\n")
                f.write("|---:|---:|---:|---:|---:|---:|---:|\n")

                for _, r in sub.iterrows():
                    f.write(
                        f"| {int(r['rank'])} "
                        f"| {int(r['feature_index'])} "
                        f"| {r['mean_diff_correct_minus_wrong']:.4f} "
                        f"| {r['correct_mean_activation']:.4f} "
                        f"| {r['wrong_mean_activation']:.4f} "
                        f"| {r['correct_activation_frequency']:.3f} "
                        f"| {r['wrong_activation_frequency']:.3f} |\n"
                    )

                f.write("\n")

    print("Saved:", args.output)


if __name__ == "__main__":
    main()
