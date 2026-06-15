import argparse
import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="outputs/tiny_prompt_outputs.csv")
    parser.add_argument("--output", default="outputs/switching_facts.csv")
    args = parser.parse_args()

    df = pd.read_csv(args.input)

    if "is_correct" not in df.columns:
        raise ValueError("Input CSV must contain an is_correct column.")

    df["is_correct"] = df["is_correct"].astype(str).str.lower().isin(["true", "1", "yes"])

    summary = (
        df.groupby("fact_id")
        .agg(
            n_variants=("variant_id", "count"),
            n_correct=("is_correct", "sum"),
            n_wrong=("is_correct", lambda x: (~x).sum()),
        )
        .reset_index()
    )

    switching = summary[(summary["n_correct"] > 0) & (summary["n_wrong"] > 0)]

    print("Total facts:", len(summary))
    print("Switching facts:", len(switching))
    print()
    print(switching)

    switch_df = df[df["fact_id"].isin(switching["fact_id"])].copy()
    switch_df.to_csv(args.output, index=False)

    print(f"\nSaved switching rows to {args.output}")


if __name__ == "__main__":
    main()
