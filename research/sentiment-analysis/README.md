# Sentiment Analysis: Classic NLP vs. LLMs

**Research stage:** Literature review and experimental design  
**Last updated:** 6 October 2026

## Research question

Sentiment analysis once relied mainly on word counts, TF-IDF features, and
supervised classifiers. Generative LLMs can now assign sentiment through a
prompt. Under what conditions do classical methods remain preferable in 2026?

The working conclusion is that model selection depends on the task definition,
available labels, domain, and operational requirements. Sparse linear models
remain useful for stable, high-volume classification. Prompted LLMs offer
flexibility when labels are scarce or outputs require richer context. Trained
transformer classifiers, compressed encoders, and hybrid systems provide
important alternatives between these families.

**Begin with the [literature review](literature/review.md)**, then use the
[evidence ledger](literature/evidence-ledger.md) to examine the support for its
claims.

## Scope

- **Problem:** Polarity, targets, aspects, subjectivity, stance, and intensity;
  negation, sarcasm, implicit opinions, annotation ambiguity, and domain shift.
- **Methods:** Lexicons and rules, sparse supervised learning, earlier neural
  architectures, contextual encoders, prompted LLMs, and hybrids.
- **Tradeoffs:** Predictive quality, annotation effort, cost, latency,
  interpretability, reproducibility, privacy, and deployment control.
- **Applications:** Financial news and filings, consumer feedback, and
  open-ended employee surveys.

## Method families

| Family | Representative approaches | Main research consideration |
|---|---|---|
| Lexicons and rules | VADER, Loughran–McDonald, SentiWordNet | Transparent measurement versus contextual coverage |
| Sparse supervised models | TF-IDF with Naive Bayes, logistic regression, LinearSVC, NB-SVM | Strong efficient baselines versus semantic generalization |
| Neural and contextual classifiers | CNNs/LSTMs, BERT, RoBERTa, FinBERT | Learned representations and domain-specific supervision |
| Compact and few-shot encoders | DistilBERT, TinyBERT, SetFit | Contextual modeling under data and compute constraints |
| Generative and hybrid systems | Zero/few-shot LLMs, financial adaptation, selective escalation | Flexible analysis versus operating cost and reliability |

The [method comparison](methodology/method-comparison.csv) contains 14 entries
with mechanisms, supervision needs, limitations, use cases, and source IDs.

## Research materials

| Material | Contents |
|---|---|
| [Literature review](literature/review.md) | Technical explanation of the problem, methods, financial relevance, and selection criteria |
| [Evidence ledger](literature/evidence-ledger.md) | 16 evidence entries linking findings to sources, conditions, and limitations |
| [Additional findings](literature/additional-findings.md) | SentiWordNet, compression evidence, target-specific finance, governance, and survey applications |
| [Annotated reading list](literature/reading-list.md) | Primary sources, direct paper links, reading notes, and review depth |
| [Evaluation protocol](methodology/evaluation-protocol.md) | Proposed datasets, baselines, leakage controls, metrics, and operational measurements |
| [Implementation resources](resources/implementations.md) | Upstream code, model checkpoints, datasets, and reproducibility considerations |
| [Source records](sources/README.md) | 42 verified source records, bibliography, retrieval provenance, and repository revisions |
| [Draft archive](archive/README.md) | Preserved draft and citation-integration record |

## Progress

| Workstream | Status | Available output |
|---|---|---|
| Problem definition and method taxonomy | Documented | Literature review and method comparison |
| Targeted literature review | Completed for the current scope | 42 sources; eight PDF papers and one HTML article inspected beyond their abstracts |
| Comparative evidence and limitations | Documented | Evidence ledger and additional findings |
| Evaluation design | Prepared | Protocol covering quality, robustness, calibration, cost, and latency |
| Dataset preparation and model execution | Planned | Candidate datasets and systems identified in the protocol |
| Benchmark results and trading evaluation | Pending | No locally measured results reported |

## Selected starting references

| Reference | Contribution |
|---|---|
| [R03 — Wang & Manning, 2012](literature/reading-list.md#r03) | Strong classical sentiment baselines and the value of bigrams |
| [R12 — Araci, 2019](literature/reading-list.md#r12) | Financial sentiment classification with FinBERT |
| [R13 — Zhang et al., 2024](literature/reading-list.md#r13) | LLM comparison across 13 tasks and 26 datasets |
| [R25 — Srirag et al., 2025](literature/reading-list.md#r25) | Sentiment and sarcasm across English varieties |
| [R27 — Li et al., 2026](literature/reading-list.md#r27) | Prompt sensitivity and internal sentiment mechanisms |
| [R40 — Muhammad et al., 2026](literature/reading-list.md#r40) | Target-based financial sentiment benchmark |

## Next research steps

1. Select the primary dataset and define the target, label policy, and holdout
   procedure.
2. Compare a strong sparse baseline, a contextual classifier, and prompted LLMs
   under the same input and evaluation contract.
3. Measure error slices, uncertainty, calibration, latency, and total cost;
   assess whether selective escalation improves the combined system.

## Evidence and reproducibility

Reference IDs **R01–R42** are consistent across the reading list, source catalog,
BibTeX bibliography, evidence ledger, and method comparison. Quantitative
findings belong to the cited studies; engineering recommendations are synthesis.
The scope is a targeted review rather than an exhaustive model ranking.

The current materials establish the literature and experimental design.
Benchmarking, model training, and trading backtests have not been performed.
