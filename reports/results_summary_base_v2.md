# Results summary: Base Gemma switching-fact analysis

## Goal

This experiment tests whether different prompt/tokenization variants of the same factual question can lead to different model behavior, and whether those differences are visible in hidden states and Gemma Scope SAE features.

The main comparison is not random correct vs wrong questions. The comparison is within the same fact:

- same factual question
- multiple prompt variants
- some variants answered correctly
- some variants answered incorrectly

## Model and SAE setup

- Model: `google/gemma-2-2b`
- SAE: Gemma Scope 2B PT residual SAE
- Layers analyzed: 6, 9, 12

The base Gemma model is used because it matches the Gemma Scope 2B PT SAE better than the instruction-tuned model.

## Full switching-fact analysis

The full analysis found switching facts where prompt variants of the same fact produced both correct and wrong answers.

Initial SAE analysis showed that correct and wrong variants activate different sparse feature patterns. However, inspection of top activating examples showed that many strong SAE features were related to repetition or prompt-copying behavior.

This means the full analysis captured an important failure mode, but not only factual retrieval errors.

## Failure-mode filtering

Generated answers were classified into failure types. Repetition and instruction-copy failures were removed to create a cleaner subset.

After cleaning:

- clean rows: 111
- clean switching facts: 8
- clean switching rows used for hidden-state extraction: 18
- activation rows across layers 6, 9, 12: 54

## Clean hidden-state result

The clean hidden-state analysis still showed separation between correct and wrong variants, but the delta baseline was limited because only one clean fact had enough correct-correct pairs for a reliable per-fact delta.

Therefore, the clean hidden-state result is useful but should be treated as preliminary.

## Clean SAE result

In SAE feature space, correct-vs-wrong pairs were farther apart than correct-vs-correct pairs across all tested layers.

| Layer | correct_correct SAE cosine distance | correct_wrong SAE cosine distance |
|---:|---:|---:|
| 6 | 0.0685 | 0.1568 |
| 9 | 0.1023 | 0.2331 |
| 12 | 0.2312 | 0.2642 |

This suggests that even after removing repetition/prompt-copy failures, successful and failed variants of the same fact still differ in sparse SAE feature space.

## Interpretation

The results support the idea that prompt/tokenization variants can change the internal representation of factual questions.

Two effects appear:

1. Some prompt variants push the base model into degenerate repetition or prompt-copying behavior.
2. Even after filtering those cases, correct and wrong factual variants still show differences in SAE feature space.

This does not prove that tokenization alone causes factual failure. Prompt wording and instruction format are still mixed with tokenization. However, the pipeline provides evidence that correctness-changing prompt variants are represented differently inside the model.

## Current limitations

- The clean subset is small.
- Prompt wording and tokenization are not fully separated yet.
- SAE feature IDs are associated with correct/wrong behavior, but their human-readable meanings still need interpretation.
- More facts and more controlled tokenization variants are needed for stronger statistical conclusions.

## Next steps

1. Increase the number of clean switching facts.
2. Create stricter tokenization-controlled variants where wording is minimally changed.
3. Inspect top SAE features using top activating examples or external feature dashboards.
4. Compare feature behavior across layers and prompt types.
