# Constructed-fixture execution records

Executed **6 October 2026** with Python 3.12, scikit-learn 1.5.2, NumPy 1.26.4,
and vaderSentiment 3.3.2. The local virtual environment inherited available
Python 3.12 packages and installed vaderSentiment; complete fresh-environment
installation was not tested. Per-run JSON records preserve exact package and
platform versions and UTC timestamps.

## Scope

These are actual local runs on [constructed fixtures](../../code/data/smoke/README.md):
18 training rows and nine test rows, balanced across three labels. Sentences are
simple, vocabulary overlaps, and labels are authored rather than independently
annotated. The results verify code execution and artifact structure. They do not
estimate performance on natural financial text or justify a model ranking.

All three classes contribute to macro F1; undefined scores are zero. The
majority baseline breaks the balanced-training tie in favor of negative. VADER
uses its standard compound-score thresholds and receives no label-based fitting.

| Execution | Accuracy | Macro F1 | Saved artifacts |
|---|---:|---:|---|
| majority | 0.3333 | 0.1667 | [JSON](majority/metrics.json) · [Predictions](majority/predictions.csv) |
| logreg-word | 1.0000 | 1.0000 | [JSON](logreg-word/metrics.json) · [Predictions](logreg-word/predictions.csv) |
| linearsvc-word | 1.0000 | 1.0000 | [JSON](linearsvc-word/metrics.json) · [Predictions](linearsvc-word/predictions.csv) |
| linearsvc-char | 1.0000 | 1.0000 | [JSON](linearsvc-char/metrics.json) · [Predictions](linearsvc-char/predictions.csv) |
| vader | 1.0000 | 1.0000 | [JSON](vader/metrics.json) · [Predictions](vader/predictions.csv) |

## Reproduction

From `research/sentiment-analysis/code/`, follow the [setup](../../code/README.md#setup).
The recorded commands below use existing output directories. To rerun, change
`--output` to a fresh directory under `../results/local/`; the CLI intentionally
refuses to overwrite existing artifacts.

```bash
python -m sentiment --model majority --features word --train data/smoke/train.csv --test data/smoke/test.csv --purpose smoke --dataset-note "Original constructed examples: whole-text polarity; 18 training and 9 test rows; balanced classes; fixed separate splits; not a representative benchmark" --output ../results/smoke/majority
python -m sentiment --model logreg --features word --train data/smoke/train.csv --test data/smoke/test.csv --purpose smoke --dataset-note "Original constructed examples: whole-text polarity; 18 training and 9 test rows; balanced classes; fixed separate splits; not a representative benchmark" --output ../results/smoke/logreg-word
python -m sentiment --model linearsvc --features word --train data/smoke/train.csv --test data/smoke/test.csv --purpose smoke --dataset-note "Original constructed examples: whole-text polarity; 18 training and 9 test rows; balanced classes; fixed separate splits; not a representative benchmark" --output ../results/smoke/linearsvc-word
python -m sentiment --model linearsvc --features char --train data/smoke/train.csv --test data/smoke/test.csv --purpose smoke --dataset-note "Original constructed examples: whole-text polarity; 18 training and 9 test rows; balanced classes; fixed separate splits; not a representative benchmark" --output ../results/smoke/linearsvc-char
python -m sentiment --model vader --features word --train data/smoke/train.csv --test data/smoke/test.csv --purpose smoke --dataset-note "Original constructed examples: whole-text polarity; 18 training and 9 test rows; balanced classes; fixed separate splits; not a representative benchmark" --output ../results/smoke/vader
```

## Validation and limits

The automated suite checks malformed data, duplicate/overlapping examples,
group separation, training-only vocabulary, fixed metric ordering, imported
prediction alignment, pinned-checkpoint requirements, and output preservation.
No pretrained FinBERT weights or LLM API were executed. The imported scorer was
checked with constructed predictions. Timings in each JSON cover one local run;
they do not measure request latency distributions, production cost, or energy.

Real-data dataset preparation, development-set tuning, uncertainty estimation,
calibration, shifted-domain testing, and controlled LLM comparisons remain
pending in [Experiments](../../EXPERIMENTS.md).
