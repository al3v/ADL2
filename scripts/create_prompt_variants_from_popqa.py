import argparse
import pandas as pd


def make_variants(question):
    question = str(question).strip()

    variants = [
        ("original", question),
        ("short_direct", question.replace("Who was", "Who is").replace("What is", "What is")),
        ("answer_briefly", question + " Answer briefly."),
        ("no_explanation", question + " Give only the answer."),
        ("direct_answer", "Directly answer this factual question: " + question),
    ]

    seen = set()
    clean_variants = []
    for variant_id, q in variants:
        q = " ".join(q.split())
        if q not in seen:
            clean_variants.append((variant_id, q))
            seen.add(q)

    return clean_variants


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="~/ADL-SAE-old/data/popqa_balanced_clean_60.csv",
    )
    parser.add_argument(
        "--output",
        default="data/prompt_variants.csv",
    )
    args = parser.parse_args()

    df = pd.read_csv(args.input.replace("~", "/dss/dsshome1/01/ra94tad2"))

    rows = []

    for i, row in df.iterrows():
        fact_id = f"fact_{i:04d}"
        original_question = row["question"]

        for variant_id, question in make_variants(original_question):
            rows.append({
                "fact_id": fact_id,
                "variant_id": variant_id,
                "question": question,
                "original_question": original_question,
                "correct_answer": row["correct_answer"],
                "possible_answers": row.get("possible_answers", ""),
                "type": row.get("type", ""),
            })

    out = pd.DataFrame(rows)
    out.to_csv(args.output, index=False)

    print("Saved:", args.output)
    print("Facts:", out["fact_id"].nunique())
    print("Rows:", len(out))
    print(out.head())


if __name__ == "__main__":
    main()
