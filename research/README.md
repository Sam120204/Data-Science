# Sentiment Analysis: Classic NLP vs. LLMs

**Research question:** Why choose classical sentiment analysis in 2026 when an
LLM can classify text through a prompt?

The research compares lexical rules, sparse classifiers, contextual transformer
classifiers, and prompted LLMs. The choice depends on the task, available labels,
quality requirements, cost, latency, and interpretability, with particular
attention to financial text.

## Start here

1. **[Research findings](RESEARCH.md)** — what sentiment analysis solves, why it
   is difficult, how the methods work, published comparisons, and practical tradeoffs.
2. **[Experiments and progress](EXPERIMENTS.md)** — implemented methods, completed
   checks, example-run results, and the planned comparison on real data.
3. **[Papers and resources](REFERENCES.md)** — annotated references with paper,
   PDF, implementation, and dataset links.
4. **[Code](code/README.md)** — runnable baselines and reproduction commands.

## Progress

| Area | Current status |
|---|---|
| Literature | 46 references reviewed at the depth recorded in the reading notes |
| Research synthesis | Task definitions, existing methods, tradeoffs, and finance/industry applications documented |
| Baseline code | Majority class, TF-IDF + logistic regression, LinearSVC, and VADER implemented |
| Execution | Five runs on constructed examples; 12 automated checks |
| Next work | Representative-data benchmarking, contextual model execution, and LLM comparison |

The example runs demonstrate implementation. They do not establish performance
on real financial text. Published study results are identified separately.

## Folder contents

```text
research/
├── README.md          # Overview and progress
├── RESEARCH.md        # Findings by subject
├── EXPERIMENTS.md     # Executed work and evaluation plan
├── REFERENCES.md      # Papers and resource links
└── code/              # Baselines, checks, and two example CSVs
```
