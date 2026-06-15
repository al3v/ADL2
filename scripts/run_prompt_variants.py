import argparse
import re
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


def normalize_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def is_correct_answer(generated_answer, correct_answer):
    generated_norm = normalize_text(generated_answer)
    correct_norm = normalize_text(correct_answer)
    return correct_norm in generated_norm


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/tiny_prompt_variants.csv")
    parser.add_argument("--output", default="outputs/tiny_prompt_outputs.csv")
    parser.add_argument("--model", default="google/gemma-2-2b-it")
    parser.add_argument("--max-new-tokens", type=int, default=40)
    args = parser.parse_args()

    print("CUDA available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))

    df = pd.read_csv(args.input)

    tokenizer = AutoTokenizer.from_pretrained(args.model)

    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        dtype=torch.float16,
        device_map="cuda",
    )

    rows = []

    for i, row in df.iterrows():
        question = row["question"]
        correct_answer = row["correct_answer"]

        inputs = tokenizer(question, return_tensors="pt").to("cuda")
        input_len = inputs["input_ids"].shape[-1]

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=args.max_new_tokens,
                do_sample=False,
                pad_token_id=tokenizer.eos_token_id,
            )

        generated_only_ids = outputs[0][input_len:]
        generated_answer = tokenizer.decode(
            generated_only_ids,
            skip_special_tokens=True,
        ).strip()

        full_output = tokenizer.decode(
            outputs[0],
            skip_special_tokens=True,
        ).strip()

        correct = is_correct_answer(generated_answer, correct_answer)

        print("=" * 80)
        print("fact_id:", row["fact_id"])
        print("variant_id:", row["variant_id"])
        print("question:", question)
        print("generated:", generated_answer)
        print("correct_answer:", correct_answer)
        print("is_correct:", correct)

        rows.append({
            "fact_id": row["fact_id"],
            "variant_id": row["variant_id"],
            "question": question,
            "correct_answer": correct_answer,
            "generated_answer": generated_answer,
            "full_output": full_output,
            "is_correct": correct,
        })

    out_df = pd.DataFrame(rows)
    out_df.to_csv(args.output, index=False)
    print(f"\nSaved outputs to {args.output}")


if __name__ == "__main__":
    main()
