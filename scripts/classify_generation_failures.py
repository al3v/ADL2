import argparse
import pandas as pd
import re


def normalize_text(x):
    x = str(x).lower()
    x = re.sub(r"\s+", " ", x)
    return x.strip()


def repeated_ngram_score(text, n=5):
    words = normalize_text(text).split()
    if len(words) < n:
        return 0.0

    ngrams = [" ".join(words[i:i+n]) for i in range(len(words)-n+1)]
    if not ngrams:
        return 0.0

    return 1.0 - (len(set(ngrams)) / len(ngrams))


def classify_row(row):
    question = normalize_text(row["question"])
    generated = normalize_text(row["generated_answer"])
    correct_answer = normalize_text(row["correct_answer"])

    if generated == "" or generated == "nan":
        return "empty"

    rep_score = repeated_ngram_score(generated, n=5)

    if rep_score > 0.35:
        return "repetition"

    if question and generated.count(question) >= 2:
        return "question_copy"

    if "give only the answer" in generated or "answer briefly" in generated:
        return "instruction_copy"

    if correct_answer and correct_answer in generated:
        return "contains_correct_answer"

    return "other_wrong_or_offtopic"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="outputs/prompt_outputs_base_v2.csv")
    parser.add_argument("--output", default="reports/generation_failure_types_base_v2.csv")
    args = parser.parse_args()

    df = pd.read_csv(args.input)

    df["failure_type"] = df.apply(classify_row, axis=1)

    df.to_csv(args.output, index=False)

    print("Saved:", args.output)
    print()
    print("Counts by correctness and failure type:")
    print(df.groupby(["is_correct", "failure_type"]).size().reset_index(name="count"))


if __name__ == "__main__":
    main()
