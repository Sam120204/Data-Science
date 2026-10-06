# Sentiment research code

Original baseline and scoring code for whole-text, three-class sentiment.
It operationalizes the methods in [Research](../RESEARCH.md) and shares the
labels and measurements described in [Experiments](../EXPERIMENTS.md).

## Implemented methods

| Runner | Mechanism | Research/source link | Execution status |
|---|---|---|---|
| `majority` | Most frequent training class; ties use negative, neutral, positive order | Class-imbalance control | Smoke run saved |
| `logreg` | Training-only TF-IDF + regularized logistic regression | [Wang & Manning](https://aclanthology.org/P12-2018/); [scikit-learn](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) | Smoke run saved |
| `linearsvc` | Training-only TF-IDF + linear margin classifier | [Wang & Manning](https://aclanthology.org/P12-2018/); [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html) | Smoke run saved |
| `vader` | Lexicon/rules; compound ≥ 0.05 positive, ≤ −0.05 negative, otherwise neutral | [VADER paper](https://ojs.aaai.org/index.php/ICWSM/article/view/14550); [implementation](https://github.com/cjhutto/vaderSentiment) | Smoke run saved |
| `finbert` | CPU inference with `ProsusAI/finbert`, pinned model/tokenizer revision | [Araci](https://arxiv.org/abs/1908.10063); [checkpoint](https://huggingface.co/ProsusAI/finbert) | Adapter implemented; weights not executed |
| `imported` | Scores externally generated predictions against identical test IDs | [LLM task contract](../EXPERIMENTS.md#6-prompted-model-task-contract) | Scoring path checked; no LLM calls |

The sparse models use word unigrams/bigrams by default. `--features char` uses
character-within-word 3–5-grams instead. Both keep stopwords, including negation,
use sublinear TF, and fit vocabulary/IDF only on training data. Regularization
is fixed at `C=1`; these are starting baselines, not tuned reproductions of
NB-SVM or the cited papers. SVM margins and VADER compound scores are not treated
as calibrated probabilities.

## Setup

Run from `research/sentiment-analysis/code/`. Python 3.10–3.12 is recommended for
the recorded dependency versions.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

The requirements pin the versions used for the stored smoke runs. Fresh
installation on every platform has not been verified. FinBERT is optional:

```bash
python -m pip install -r requirements-transformers.txt
```

## Run the constructed example

```bash
python -m sentiment --model logreg \
  --train data/smoke/train.csv --test data/smoke/test.csv \
  --purpose smoke --dataset-note "Constructed fixtures; whole-text polarity; predefined separate splits" \
  --output ../results/local/logreg-smoke
```

Change `--model` to `linearsvc`, `majority`, or `vader`. VADER does not train;
supplying `--train` still checks split overlap and records its provenance. Select
a fresh output directory for every run; existing artifacts are never overwritten.
Stored executions are in [results/smoke](../results/smoke/README.md).

## Bring a research dataset

Use UTF-8 CSV files with `id,text,label` and optional `group_id`. Allowed labels
are exactly `negative`, `neutral`, and `positive`. Each row must have nonempty
ID/text, and training data must contain all three classes. Preserve official
labels and document any conversion. For multiple targets in one article, use
the same `group_id` when preparing splits; this runner does not model targets.

```bash
python -m sentiment --model linearsvc --features char \
  --train /path/to/train.csv --test /path/to/test.csv \
  --purpose benchmark --dataset-note "Dataset version, agreement subset, labeling rubric, split policy" \
  --output ../results/local/linearsvc-benchmark
```

The `benchmark` flag records intended use; it does not validate dataset quality
or certify the experiment. Keep development/tuning data separate. The input
checks detect exact normalized overlap, not paraphrases, syndicated near-copies,
pretraining contamination, or chronological leakage. Audit those separately.

FinBERT requires an immutable 40-character commit SHA from the checkpoint's
revision history. It downloads model/tokenizer files on first use; no model
weights are included in this repository.

```bash
python -m sentiment --model finbert --revision MODEL_COMMIT_SHA \
  --test /path/to/test.csv --batch-size 16 \
  --purpose benchmark --dataset-note "Independent financial holdout; checkpoint training-overlap audit documented" \
  --output ../results/local/finbert-benchmark
```

Replace `MODEL_COMMIT_SHA` before running. The adapter verifies checkpoint label
names and truncates at 512 tokens. Audit long-text coverage and the checkpoint's
Financial PhraseBank training overlap before using its results as a comparison.
It provides whole-text polarity, not aspect/target extraction.

## Score external or LLM predictions

Create a CSV with `id,prediction`, one valid label per test item. Order may vary;
the scorer aligns IDs and rejects missing, extra, repeated, or invalid labels.

```bash
python -m sentiment --model imported --revision "model-version/prompt-version" \
  --test /path/to/test.csv --predictions /path/to/predictions.csv \
  --purpose benchmark --dataset-note "Dataset/split; generation settings and prompt recorded with raw responses" \
  --output ../results/local/llm-benchmark
```

This code makes no API requests. Archive prompts, demonstrations, raw responses,
decoding settings, retries, invalid outputs, and token usage separately. Strict
scoring refuses an incomplete prediction file; do not silently drop failed
responses to make it pass. The current runner has no abstention/invalid-response
metric. Implement that policy before a study where unresolved responses occur.

## Outputs and current limits

Every run writes `metrics.json` and `predictions.csv`. JSON records model
settings, dependency versions, platform, dataset hashes and class counts,
purpose, dataset note, accuracy, macro F1, per-class measures, and the confusion
matrix. All three classes contribute to macro F1; undefined values use zero.
CSV records test IDs, true labels, predictions, and correctness, without text.

Local initialization, fit, and full-test prediction timings describe one run.
They are not per-request p50/p95 latency, a throughput benchmark, energy use,
or operating cost. The code does not yet implement calibration, confidence
intervals, hyperparameter search, target-aware extraction, LLM generation,
SetFit, distillation, or cascades. See [Experiments](../EXPERIMENTS.md) for the
complete research design and pending measurements.

The code is original and covered by the repository's MIT license. Dependencies,
model weights, and external datasets retain their own terms. Upstream references
and recorded repository revisions are in [References](../REFERENCES.md) and
[repository snapshots](../sources/repository-snapshots.json).
