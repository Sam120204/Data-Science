# Additional findings

Last updated: **6 October 2026**.

This companion to the [literature review](review.md) examines word-sense lexical
resources, model compression, a target-specific financial benchmark,
trustworthiness criteria, and survey applications. Source checks and draft
provenance are documented in the [archive](../archive/README.md).

## 1. A word-sense lexicon: SentiWordNet

[SentiWordNet 3.0, R38](https://aclanthology.org/L10-1531/) adds a useful example
beyond VADER and financial word lists. It annotates **WordNet synsets** with
positivity, negativity, and objectivity/neutrality scores. A synset represents a
word sense, rather than treating every occurrence of a spelling as equivalent.

This introduces a further technical distinction: lexical sentiment resources
can operate on word senses, but a system must still decide which sense applies
to an occurrence in context and how to aggregate scores. A sense-aware lexicon
does not automatically solve negation scope, sarcasm, or aspect attribution.
The main report and comparison CSV now include this distinction.

## 2. Compression provides another practical middle option

The original paper abstracts report the following compression figures:

| Source | Reported historical result | Scope |
|---|---|---|
| [DistilBERT, R11](https://arxiv.org/abs/1910.01108) | 40% size reduction, retention of 97% of BERT's language-understanding capability, and 60% faster operation in the paper's evaluation | General language-model distillation; not a universal sentiment timing result |
| [TinyBERT, R39](https://aclanthology.org/2020.findings-emnlp.372/) | Four-layer student retains more than 96.8% of its BERT-Base teacher's GLUE performance, with a model 7.5 times smaller and inference 9.4 times faster | Specific model, benchmark, and experimental configuration |

These numbers motivate including compressed encoders. They should not be used
to infer current latency on different hardware, a particular financial corpus,
or performance relative to a prompted LLM. Retaining 96.8% of a teacher's GLUE
performance is also different from achieving 96.8% sentiment accuracy.

## 3. A target-specific financial benchmark with a strong reported LLM result

The most consequential empirical addition is
[Muhammad et al., R40](https://link.springer.com/article/10.1007/s41060-026-01201-x).
The inspected journal version was published **2 July 2026** and cites an earlier
2025 CLiC-it conference version. Its citation metadata also carries a December
2026 issue date; the bibliography records the earlier online publication date
and preserves the issue date separately.

The dataset concerns Alphabet, Amazon, Netflix, and Nvidia, with news from
4 September 2023 through 30 January 2024. After excluding articles with no target,
it contains **1,162 Bloomberg articles** and **1,334 target-specific sentiment
annotation cases**. Multiple entities can occur in one article, so these counts
describe different units. The labels represent an investor viewpoint under the
paper's annotation guidelines.

The paper's §4.1 and Table 3 report:

| Evaluated system | Setting | Reported macro F1 |
|---|---|---:|
| VADER | Lexicon/rules | 0.37 |
| FinBERT | Financial encoder baseline | 0.54 |
| DeBERTa-v3-ABSA | Target/aspect model, fivefold cross-validation | 0.66 |
| DeepSeek-R1 | Zero-shot | 0.81 |
| ChatGPT-o1 | Five-shot | 0.86 |
| DeepSeek-R1 | Five-shot | 0.87 |

This is evidence of a reported LLM advantage in a specific target-aware task.
It complements R13's results on structured extraction and scarce labels; the
papers evaluate different tasks, datasets, models, and supervision settings.

Interpretation requires several qualifications:

- The source contains four companies and one historical time window. It cannot
  establish general financial-domain superiority.
- Several baseline models classify sentence/document sentiment rather than
  being designed for the target-aware contract. The paper acknowledges this
  difference. It also omits strong TF-IDF + linear classifier baselines.
- The annotation-agreement exercise uses a shared subset of 150 cases; most
  remaining cases are individually labeled. Agreement on the shared subset is
  informative but is not a guarantee of all labels' correctness.
- Only article metadata/URLs are publicly released. Full Bloomberg content
  requires the appropriate access, which limits convenient reproduction.
- The paper uses multiple serving interfaces and default settings. These are
  less controlled than pinned model revisions with a common recorded decoding
  configuration.
- Table 3 contains a consistency issue: Llama 3 8B's one-shot accuracy is 0.52
  but weighted recall is 0.40. For standard single-label classification over the
  same examples and labels, support-weighted recall equals accuracy. This flags
  a reporting/evaluation detail requiring clarification; it does not establish
  that the separate DeepSeek F1 figure is incorrect.
- Its return analysis concerns contemporaneous daily sentiment/return
  relationships. Such relationships do not establish causal effects or a
  future-return strategy with transaction costs. Model training after the news
  period also warrants care in any historical decision simulation.

The reported 0.87 figure has been checked against the publisher's full text and
table. The experiment itself has not been reproduced in this repository.

## 4. Governance gives model selection a broader technical objective

[NIST AI RMF 1.0, R41](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/)
provides an authoritative framing for the draft's discussion of validity,
reliability, transparency, explainability, privacy, and fairness. Its framework
is voluntary and does not prescribe a sentiment model family.

For this research, the useful implication is that model selection can consider
multiple measured requirements. Inspectable coefficients may make debugging
easier; a local deployment may simplify a chosen data boundary; a more capable
model may reduce consequential errors. These are properties of the complete
system and its context, not automatic certificates of trustworthiness attached
to “classic NLP” or “LLM.” A transparent classifier can still learn biased or
spurious features, and a local LLM can preserve the same deployment boundary as
a local encoder.

## 5. Survey analysis is a useful additional industry application

[Rink et al., R42](https://aclanthology.org/2024.nlp4hr-1.2/) studies aspect-based
sentiment in **1,458 Dutch employee-survey responses**, with aspects such as
salary, scheduling, communication, and personal attention. It explores Dutch
BERT-based few-shot approaches and compares them with bag-of-words and zero-shot
baselines. This is a verified application example beyond product reviews and
financial news.

This source is independently identified; it is not asserted to be the missing
reference [3] in the contributed draft. Its abstract supports the application
and setup, but does not support a claim that prompted generative LLMs universally
outperform other methods on surveys.

## 6. Task definition and questions for technical follow-up

The literature review distinguishes subjectivity detection, intensity/regression, and
stance explicit alongside sentiment polarity. In particular:

- **Subjectivity is different from polarity.** A factual sentence can have an
  unfavorable economic implication without expressing a writer's opinion.
- **A continuous intensity score needs its own rubric.** Scores from different
  lexicons, classifiers, and annotators are not automatically comparable.
- **Stance identifies support/opposition toward a proposition.** It is not
  interchangeable with positive/negative emotional tone.
- **TF-IDF is a representation.** It does not make a prediction until a
  classifier consumes it.
- **Few-shot can mean two different operations.** Prompt demonstrations usually
  leave weights fixed; supervised few-shot adaptation updates weights.
- **Readable explanations need separate checks.** A fluent rationale does not
  prove a faithful internal computation.
- **Annotator agreement is not a strict mathematical ceiling on model accuracy.**
  It characterizes reliability and ambiguity under the annotation design. The
  apparent ceiling also depends on adjudication, labels, and how predictions
  are scored.

The evaluation protocol also now includes optional deployment-footprint
measurement, explicit checks for commands embedded in input text, and a clearer
warning about annotation agreement. These additions extend the existing design;
no experiments or new deployment requirements were introduced.
