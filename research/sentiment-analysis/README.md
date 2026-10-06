# Sentiment Analysis: Classic NLP vs. LLMs

**Last updated:** 6 October 2026  
**Stage:** Literature synthesis, baseline implementation, and smoke execution

## Research question

When do classical sentiment methods remain preferable to prompted LLMs in 2026?

The working conclusion is conditional: sparse linear models can be useful for
stable, high-volume tasks with representative labels; LLMs offer flexibility
when labels are scarce or outputs need richer contextual analysis. Fine-tuned
encoders, compact models, and hybrids are essential alternatives. The choice
requires measurement on the intended data.

## Reading guide

| Document | What it covers |
|---|---|
| [Research](RESEARCH.md) | Task definition and linguistic difficulty; how existing methods work; comparative evidence; operational tradeoffs; finance and industry relevance |
| [Experiments](EXPERIMENTS.md) | Implemented code and execution status; dataset choices; fair splits; quality, robustness, calibration, latency, and cost measurements |
| [References](REFERENCES.md) | Annotated papers with primary/PDF links; upstream implementations, model checkpoints, and dataset resources |
| [Code guide](code/README.md) | Setup, baseline commands, CSV format, scoring, run artifacts, and implementation limits |

The research is consolidated by subject. Qualifications appear alongside the
findings they concern, including the target-based finance benchmark, compression
results, governance considerations, and survey applications.

## Repository structure

```text
research/sentiment-analysis/
├── README.md
├── RESEARCH.md
├── EXPERIMENTS.md
├── REFERENCES.md
├── method-comparison.csv
├── code/
│   ├── README.md
│   ├── requirements.txt
│   ├── requirements-transformers.txt
│   ├── sentiment/                 # Input checks, models, scoring, CLI
│   ├── tests/                     # Leakage and artifact integrity checks
│   └── data/smoke/                # Explicitly constructed examples
├── results/smoke/                 # Saved executions, metrics, predictions
├── sources/                       # JSON catalog, BibTeX, evidence provenance
└── archive/                       # Original contribution preserved verbatim
```

## Progress

| Workstream | Completed output | Remaining work |
|---|---|---|
| Literature | 42 sources; eight PDF papers and one HTML article inspected beyond abstracts | Further sources as the experimental question narrows |
| Methods and evidence | [14-method comparison](method-comparison.csv); qualified findings integrated in Research | Test conclusions on intended data |
| Classical code | TF-IDF + logistic regression, LinearSVC, majority baseline, word/character features | Development-set tuning and repeated support-set experiments |
| Lexicon code | VADER inference and common scoring | Financial dictionary baseline and domain-validity assessment |
| Contextual code | FinBERT adapter requiring pinned checkpoint revision | Model-weight execution and checkpoint/benchmark overlap audit |
| LLM comparison support | Prompt contract and strict external-prediction scorer | Prompt validation, model execution, raw-response/invalid-output accounting |
| Local execution | [Constructed-example smoke records](results/smoke/README.md) and automated validation checks | Representative-data quality and operational measurements |

## Selected papers

- [Wang & Manning (2012): Baselines and Bigrams](https://aclanthology.org/P12-2018/) — strong classical baseline design.
- [Araci (2019): FinBERT](https://arxiv.org/abs/1908.10063) — financial contextual classification.
- [Zhang et al. (2024): LLM sentiment evaluation](https://aclanthology.org/2024.findings-naacl.246/) — 13 tasks and 26 datasets, with task-dependent results.
- [Srirag et al. (2025): BESSTIE](https://aclanthology.org/2025.findings-acl.441/) — sentiment and sarcasm across English varieties.
- [Li et al. (2026): Sentiment circuit analysis](https://aclanthology.org/2026.acl-long.928/) — prompt sensitivity and mechanistic interventions.
- [Muhammad et al. (2026): Target-based financial sentiment](https://link.springer.com/article/10.1007/s41060-026-01201-x) — a strong reported LLM result with important task and reproducibility qualifications.

Complete citations and available PDFs are in [References](REFERENCES.md).
Reference IDs R01–R42 match the source catalog and BibTeX bibliography. Detailed
source audit locators remain in [evidence notes](sources/evidence-notes.json).

## Next experiment

Select a dataset and label policy, preserve a clean holdout, tune on development
examples, and compare strong sparse baselines, a contextual classifier, and
prompted LLMs under identical labels and permitted context. Report error slices
and uncertainty alongside operational measurements. No representative sentiment
benchmark, LLM API experiment, or trading backtest has yet been completed.
