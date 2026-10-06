# Sentiment baselines

Runnable starting points for **whole-text, three-class polarity**: `negative`,
`neutral`, and `positive`. See [Experiments](../EXPERIMENTS.md) for completed
checks, recorded example scores, and the evaluation plan.

## Files

| File | Purpose |
|---|---|
| [run.py](run.py) | Command-line entry point |
| [models.py](models.py) | Majority, sparse classifiers, VADER, and optional FinBERT |
| [data.py](data.py) | CSV validation and split-overlap checks |
| [evaluate.py](evaluate.py) | Shared metrics and run-output writing |
| [test_baselines.py](test_baselines.py) | 12 automated checks |
| [examples/train.csv](examples/train.csv), [examples/test.csv](examples/test.csv) | 18 constructed training rows and nine test rows |

## Setup and run

From `research/code/`, using Python 3.12:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest test_baselines -v

python run.py --model logreg \
  --train examples/train.csv --test examples/test.csv \
  --purpose smoke --dataset-note "Constructed examples; whole-text polarity; fixed separate splits" \
  --output runs/logreg-example
```

Change `--model` to `majority`, `linearsvc`, or `vader`. For character features,
add `--features char` to a sparse-model run. Use a new output directory each time;
existing outputs are never overwritten. `runs/` is ignored by Git so rerunning
examples does not clutter the research folder.

The example CSVs were authored for execution checks, have equal class support,
and use deliberately simple sentences with overlapping vocabulary. They are not
sampled from a published dataset or independently annotated. Their scores cannot
establish research performance or financial-domain generalization.

## Methods

| Model | Implementation | Source |
|---|---|---|
| `majority` | Most frequent training class; ties resolve negative, neutral, positive | Class-imbalance control |
| `logreg` | TF-IDF + logistic regression | [Strong classical baseline design](https://aclanthology.org/P12-2018/) |
| `linearsvc` | TF-IDF + linear SVM | [scikit-learn text features](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) |
| `vader` | Lexicon/rules with standard ±0.05 compound thresholds | [VADER paper](https://ojs.aaai.org/index.php/ICWSM/article/view/14550) |
| `finbert` | Optional CPU inference; immutable checkpoint revision required | [FinBERT paper](https://arxiv.org/abs/1908.10063), [checkpoint](https://huggingface.co/ProsusAI/finbert) |
| `imported` | Scores predictions generated outside this script | [LLM task contract](../EXPERIMENTS.md#6-prompted-model-task-contract) |

Sparse models use word unigrams/bigrams or character-within-word 3–5-grams,
sublinear TF, no stopword removal, and fixed `C=1`. Vocabulary and IDF are fitted
only on training data. These are starting baselines, not tuned reproductions of
NB-SVM. VADER scores and SVM margins are not calibrated probabilities.

## Use a real dataset

Supply UTF-8 CSVs with `id,text,label`; optional `group_id` keeps related
articles/events in one split. The runner rejects missing values, invalid labels,
duplicate IDs/text, and train/test overlap in IDs, normalized text, or groups.
Training data must contain all three classes. Near-duplicates, chronology, and
pretraining contamination require separate dataset audits.

Replace the example paths, select `--purpose benchmark`, and describe the dataset
version, rubric, and split in `--dataset-note`. That flag records intent; it does
not certify the experiment. Tune on development data, not the test set.

For optional FinBERT, install `requirements-transformers.txt`, choose `--model
finbert`, and supply `--revision` with a 40-character checkpoint commit SHA.
Model files download on first use. The adapter checks label names and truncates
at 512 tokens. Audit checkpoint training overlap and long-text coverage.
FinBERT weights have not yet been executed in this project.

For external predictions, choose `--model imported`, supply an `id,prediction`
CSV through `--predictions`, and record the model/prompt version in `--revision`.
IDs must match the test set exactly. No API requests are made by this code.
Preserve prompts, raw responses, decoding settings, and invalid-output counts
when conducting an LLM experiment; the scorer currently requires one valid
prediction per item and does not implement abstention scoring.

## Outputs

Each execution writes `metrics.json` and `predictions.csv` in the chosen output
directory. Records include dataset hashes, settings, package versions, accuracy,
macro F1, per-class metrics, and the confusion matrix. All three classes contribute
to macro F1; undefined values use zero. Timings cover one local initialization,
fit, and batch prediction, rather than production latency distributions or cost.

Calibration, confidence intervals, target-aware extraction, and LLM generation
remain future work. Dependency versions match the initial runs; fresh installation
on every platform has not been verified. Original code follows the repository's
MIT license; dependencies, external datasets, and model weights retain their own terms.
