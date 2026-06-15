import argparse
import pandas as pd
import matplotlib.pyplot as plt


def to_bool(x):
    return str(x).lower() in ["true", "1", "yes"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pair-input", default="reports/activation_pair_type_summary_v1.csv")
    parser.add_argument("--token-input", default="reports/tokenization_switching_v1.csv")
    parser.add_argument("--delta-output", default="reports/activation_distance_delta_v1.csv")
    parser.add_argument("--delta-summary-output", default="reports/activation_distance_delta_summary_v1.csv")
    parser.add_argument("--token-summary-output", default="reports/token_count_correctness_summary_v1.csv")
    parser.add_argument("--plot-output", default="reports/activation_distance_delta_v1.png")
    args = parser.parse_args()

    pair_df = pd.read_csv(args.pair_input)

    mean_pair = (
        pair_df.groupby(["fact_id", "layer", "pair_type"])[["cosine_distance", "l2_distance"]]
        .mean()
        .reset_index()
    )

    pivot = mean_pair.pivot_table(
        index=["fact_id", "layer"],
        columns="pair_type",
        values=["cosine_distance", "l2_distance"],
    )

    pivot.columns = [f"{metric}_{pair_type}" for metric, pair_type in pivot.columns]
    pivot = pivot.reset_index()

    required = [
        "cosine_distance_correct_wrong",
        "cosine_distance_correct_correct",
        "l2_distance_correct_wrong",
        "l2_distance_correct_correct",
    ]

    for col in required:
        if col not in pivot.columns:
            pivot[col] = pd.NA

    delta_df = pivot.dropna(subset=[
        "cosine_distance_correct_wrong",
        "cosine_distance_correct_correct",
    ]).copy()

    delta_df["cosine_delta_cw_minus_cc"] = (
        delta_df["cosine_distance_correct_wrong"]
        - delta_df["cosine_distance_correct_correct"]
    )

    delta_df["l2_delta_cw_minus_cc"] = (
        delta_df["l2_distance_correct_wrong"]
        - delta_df["l2_distance_correct_correct"]
    )

    if "cosine_distance_wrong_wrong" in delta_df.columns:
        delta_df["cosine_delta_cw_minus_ww"] = (
            delta_df["cosine_distance_correct_wrong"]
            - delta_df["cosine_distance_wrong_wrong"]
        )

    if "l2_distance_wrong_wrong" in delta_df.columns:
        delta_df["l2_delta_cw_minus_ww"] = (
            delta_df["l2_distance_correct_wrong"]
            - delta_df["l2_distance_wrong_wrong"]
        )

    delta_df.to_csv(args.delta_output, index=False)

    delta_summary = (
        delta_df.groupby("layer")
        .agg(
            n_facts=("fact_id", "nunique"),
            mean_cosine_delta_cw_minus_cc=("cosine_delta_cw_minus_cc", "mean"),
            median_cosine_delta_cw_minus_cc=("cosine_delta_cw_minus_cc", "median"),
            fraction_positive_cosine_delta=("cosine_delta_cw_minus_cc", lambda x: (x > 0).mean()),
            mean_l2_delta_cw_minus_cc=("l2_delta_cw_minus_cc", "mean"),
            median_l2_delta_cw_minus_cc=("l2_delta_cw_minus_cc", "median"),
            fraction_positive_l2_delta=("l2_delta_cw_minus_cc", lambda x: (x > 0).mean()),
        )
        .reset_index()
    )

    delta_summary.to_csv(args.delta_summary_output, index=False)

    token_df = pd.read_csv(args.token_input)
    token_df["is_correct"] = token_df["is_correct"].apply(to_bool)

    token_summary = (
        token_df.groupby("is_correct")
        .agg(
            n_rows=("question", "count"),
            mean_n_tokens=("n_tokens", "mean"),
            median_n_tokens=("n_tokens", "median"),
            min_n_tokens=("n_tokens", "min"),
            max_n_tokens=("n_tokens", "max"),
        )
        .reset_index()
    )

    token_summary.to_csv(args.token_summary_output, index=False)

    plot_df = delta_summary[["layer", "mean_cosine_delta_cw_minus_cc"]].copy()

    ax = plot_df.plot(
        x="layer",
        y="mean_cosine_delta_cw_minus_cc",
        kind="bar",
        legend=False,
        figsize=(7, 4),
    )
    ax.set_title("Mean distance gap: correct-wrong minus correct-correct")
    ax.set_xlabel("Layer")
    ax.set_ylabel("Mean cosine distance gap")
    plt.tight_layout()
    plt.savefig(args.plot_output, dpi=200)

    print("Saved:", args.delta_output)
    print("Saved:", args.delta_summary_output)
    print("Saved:", args.token_summary_output)
    print("Saved:", args.plot_output)

    print()
    print("Delta summary:")
    print(delta_summary)

    print()
    print("Token count summary:")
    print(token_summary)


if __name__ == "__main__":
    main()
