# Evidence ledger

This ledger separates reported findings from interpretation. Source IDs resolve
in the [annotated reading list](reading-list.md) and
[source catalog](../sources/verified-sources.json).

**Review depth:** selected sections of eight PDF papers and one full HTML article
were inspected, along with an official framework section; other
sources were checked through abstracts, publisher metadata, official
documentation, or repository/model cards. No reported experiment was reproduced
locally. A paper's claim is not automatically an independently established fact.

## E01. A weak classical baseline can distort the comparison

- **Source:** [R03: Wang & Manning, 2012](https://aclanthology.org/P12-2018/).
- **Locator:** Abstract; §4; Tables 2–3.
- **Evidence:** Bigrams improved sentiment results in their experiments; the
  relative performance of Naive Bayes and SVM differed between snippets and
  longer reviews. NB-SVM was consistently competitive across the studied tasks.
- **Inference:** Include tuned word/character n-grams, logistic regression,
  LinearSVC, and optionally NB-SVM before claiming that classical NLP is weak.
- **Limit:** This is historical evidence about baseline design. It is not a
  head-to-head comparison with current LLMs.

## E02. Domain-specific vocabulary can invalidate generic tone measures

- **Sources:** [R36: Loughran & McDonald, 2011](https://doi.org/10.1111/j.1540-6261.2010.01625.x);
  [R05: official dictionary resource](https://sraf.nd.edu/loughranmcdonald-master-dictionary/).
- **Locator:** Publisher-supplied abstract retrieved from Crossref; official
  dictionary description.
- **Evidence:** In the paper's 1994–2008 10-K sample, almost three-fourths of
  words identified as negative by the Harvard dictionary were ordinarily not
  negative in financial usage.
- **Inference:** Domain validity is as important as algorithm choice; a generic
  dictionary may operationalize the wrong concept.
- **Limit:** This statistic concerns flagged words in one corpus and dictionary.
  It is not a document-level classifier error rate. The full journal paper was
  not inspected in this review.

## E03. FinBERT is a relevant middle option

- **Sources:** [R12: Araci, 2019](https://arxiv.org/abs/1908.10063);
  [R34: ProsusAI model card](https://huggingface.co/ProsusAI/finbert).
- **Locator:** R12 §§4–6, including §4.3 and the domain-pretraining analysis;
  R34 model description.
- **Evidence:** The paper evaluates financial sentiment with BERT-based models,
  Financial PhraseBank, and FiQA. It reports improvements over its comparison
  methods, including settings with reduced training resources.
- **Inference:** A contextual classifier trained for finance is an essential
  baseline when comparing classical models and general-purpose prompted LLMs.
- **Limit:** The paper explicitly notes that its neural baselines were not
  explored as thoroughly as BERT. It also finds relatively modest differences
  among additional domain-pretraining choices. Do not attribute every gain solely
  to financial-domain pretraining, or assume a current checkpoint exactly
  reproduces every paper result.

## E04. Prompted LLMs have strong limited-label performance, with task dependence

- **Source:** [R13: Zhang et al., NAACL Findings 2024](https://aclanthology.org/2024.findings-naacl.246/).
- **Locator:** §4.1 model setup; §5.1/Table 1; §5.3/Table 2; Appendix A.1;
  Limitations.
- **Evidence:** Evaluation covers 13 tasks and 26 datasets. The LLM group
  includes Flan-T5-XXL, Flan-UL2, text-davinci-003, and gpt-3.5-turbo. The
  supervised reference is T5-large (770M), trained with full or sampled labels.
  The paper reports a marked LLM advantage over that reference in few-shot
  settings and weaker results on several structured sentiment tasks when
  compared with the fully trained reference.
- **Concrete Table 1 examples:**

  | Task and metric | ChatGPT | Fully trained T5 |
  |---|---:|---:|
  | IMDb document classification, accuracy (%) | 94.20 | 93.93 |
  | Rest14 unified aspect-based sentiment extraction, F1 (%) | 54.46 | 75.31 |

- **Inference:** The amount of supervision and the output structure can change
  which model is preferable. “Sentiment analysis” cannot be represented by a
  single universal score.
- **Limit:** English-only datasets and older model versions. T5 is a trained
  neural model, not a TF-IDF baseline. The two rows use different metrics and
  cannot be treated as comparable absolute difficulty scores. The study's
  mixed-task average is not a universal sentiment accuracy. Appendix Table 4
  records 500 sampled test items for IMDb and Rest14 UABSA, rather than evaluating
  their entire original test sets. T5 results average three runs. The small IMDb
  score difference alone does not establish statistically superior performance.

## E05. Scarce labels do not require a large prompted model

- **Sources:** [R15: Tunstall et al., 2022](https://arxiv.org/abs/2209.11055);
  [R32: SetFit implementation](https://github.com/huggingface/setfit).
- **Locator:** Paper abstract; official repository description.
- **Evidence:** SetFit uses contrastive sentence-transformer fine-tuning and a
  classifier over embeddings, with small labeled datasets and no classification
  prompt/verbalizer.
- **Inference:** Include an efficient few-shot encoder approach when evaluating
  limited-label deployment choices.
- **Limit:** No local SetFit run or hardware comparison was performed. The
  paper's relative speed findings do not establish a universal current speedup.

## E06. Language varieties expose limitations hidden by aggregate scores

- **Source:** [R25: Srirag et al., ACL Findings 2025](https://aclanthology.org/2025.findings-acl.441/).
- **Locator:** §2 annotation/validation; experiment sections; Limitations.
- **Evidence:** BESSTIE evaluates sentiment and sarcasm in Australian, Indian,
  and British English, using Google Place reviews and Reddit comments. The paper
  reports differences across varieties and cross-variety generalization problems.
- **Inference:** Evaluation should include language varieties relevant to the
  actual users, rather than relying on a single English average.
- **Limit:** These are fine-tuned encoder/decoder experiments, not a pure
  zero-shot API benchmark. National categories simplify language variation;
  subjectivity and a limited annotation pool affect labels. Sentiment labels are
  binary after uninformative examples are discarded, so results do not establish
  three-class neutral detection performance.

## E07. A contemporary finance comparison requires methodological caution

- **Source:** [R26: Teles & Figueiredo, 2025 preprint](https://arxiv.org/abs/2510.15929).
- **Locator:** §§3.1–3.3; Tables 4–6.
- **Evidence:** Studies Financial PhraseBank, StockEmotions, and Tweet Financial
  News. Its “LLM” grouping includes generative models and pretrained encoder
  classifiers. Relative results vary: its StockEmotions per-class F1 results do
  not show a uniform generative-model advantage.
- **Review observations:** Classical models include a kernel SVC, random forest,
  and MLP. The comparison omits logistic regression and LinearSVC; classical
  preprocessing removes stopwords and reduces TF-IDF with SVD. §§3.1 and 3.2
  give inconsistent positive/neutral numeric-label mappings for TFN.
- **Inference:** Useful as a case study of how preprocessing, taxonomy, and
  dataset choice affect conclusions. It is weak evidence for a general claim
  that prompted LLMs outperform well-tuned classical sentiment pipelines.
- **Limit:** These observations are based on the paper text. Its implementation
  was not reproduced; the mapping inconsistency alone does not establish which
  mapping was actually used in code.

## E08. Prompt sensitivity has an internal-mechanism research direction in 2026

- **Source:** [R27: Li et al., ACL 2026](https://aclanthology.org/2026.acl-long.928/).
- **Locator:** §§3–4, Table 2, Appendix C, Limitations.
- **Evidence:** Uses sparse autoencoders and circuit analysis to identify
  sentiment-relevant features and amplify them at inference. The experiments
  investigate Gemma-2-2B and Llama-3.1-8B, multiple prompt templates, and seven
  datasets; samples are filtered to binary labels for transfer experiments.
- **Inference:** A representation containing sentiment information does not
  guarantee that every instruction will reliably elicit it. Mechanistic
  interventions are different from asking a model to explain its answer.
- **Limit:** Requires access to model activations and suitable pretrained sparse
  autoencoders. The paper acknowledges limited SAE availability and assumptions
  about linear representations. It does not validate every proprietary API,
  every label scheme, or all current models.

## E09. High benchmark accuracy is insufficient evidence of robustness

- **Sources:** [R18: CheckList, ACL 2020](https://aclanthology.org/2020.acl-main.442/);
  [R35: Rahul & Adebayo, workshop 2026](https://aclanthology.org/2026.dravidianlangtech-1.2/).
- **Locator:** R18 abstract; R35 Tables 1–3 and Limitations.
- **Evidence:** R18 proposes capability-oriented behavioral testing. R35 reports
  XLM-R accuracy of 99.7% on an in-distribution Hinglish test, 42.5% on a
  human-validated 400-item adversarial benchmark, and 50.8% on English TweetEval.
- **Inference:** Test negation, contrast, sarcasm, and transfer separately.
- **Limit:** R35 is a small diagnostic study of two multilingual encoders and
  does not directly compare them with prompted LLMs. It contains an incorrect
  description of 25% as chance for three-class prediction; uniform guessing is
  33.3%. Deduplication checks address some leakage routes but cannot prove all
  leakage is absent. Poor transfer after fine-tuning does not, without a
  before-fine-tuning comparison, quantify how much fine-tuning caused degradation.

## E10. Confidence and explanations need validation

- **Sources:** [R19: Guo et al., 2017](https://arxiv.org/abs/1706.04599);
  [R20: Sclar et al., 2023 preprint / ICLR 2024](https://arxiv.org/abs/2310.11324);
  R27.
- **Locator:** R19/R20 abstracts; R27 mechanism and intervention sections.
- **Evidence:** R19 studies miscalibration in modern neural networks and
  temperature scaling. R20 studies sensitivity to meaning-preserving prompt
  formatting in few-shot settings. R27 analyzes internal sentiment mechanisms.
- **Inference:** Validate confidence on held-out data, record prompt variations,
  and distinguish a generated rationale from an internal causal analysis.
- **Limit:** R20's largest reported formatting effect is not a universal
  sentiment effect. Temperature scaling addresses a calibration objective;
  it does not repair an incorrect task definition or guarantee calibration
  under arbitrary domain shift.

## E11. Financial relevance does not establish a profitable strategy

- **Sources:** [R23: SemEval financial sentiment task](https://aclanthology.org/S17-2089/);
  [R37: Tetlock, 2007](https://doi.org/10.1111/j.1540-6261.2007.01232.x).
- **Locator:** R23 abstract; R37 publisher-supplied abstract via Crossref.
- **Evidence:** Financial benchmarks target microblogs/news. Tetlock reports
  historical relationships between media pessimism, prices, and volume.
- **Inference:** Sentiment is a potentially useful measurement or feature in
  financial research. Trading value requires a separate timed, out-of-sample
  study with realistic costs.
- **Limit:** Observational relationships do not establish causality or a current
  tradable advantage. R37's full journal paper was not inspected here.

## E12. Lexical methods can distinguish word senses

- **Source:** [R38: SentiWordNet 3.0, 2010](https://aclanthology.org/L10-1531/).
- **Locator:** Abstract and source metadata.
- **Evidence:** The resource assigns polarity/objectivity scores to WordNet
  synsets, rather than simply using a single word-spelling lookup.
- **Inference:** Lexicon comparisons should identify whether their units are
  words or senses and how occurrences are mapped to those units.
- **Limit:** Resource annotation does not itself resolve contextual word sense,
  composition, or target-aware aggregation. No implementation was run here.

## E13. Compact contextual models have published efficiency evidence

- **Sources:** [R11: DistilBERT, 2019](https://arxiv.org/abs/1910.01108);
  [R39: TinyBERT, EMNLP Findings 2020](https://aclanthology.org/2020.findings-emnlp.372/).
- **Locator:** Original paper abstracts.
- **Evidence:** DistilBERT reports 40% reduced size, 97% retained
  language-understanding capability, and 60% faster operation. Four-layer
  TinyBERT reports more than 96.8% of BERT-Base's GLUE performance, with a
  7.5-times smaller model and 9.4-times faster inference.
- **Inference:** Evaluate a compressed encoder when contextual representations
  are useful but compute is constrained.
- **Limit:** These are paper-specific historical results, not sentiment-only
  accuracy, present hardware measurements, or comparisons with current prompted
  LLMs. The reported percentages describe different quantities.

## E14. A target-based financial study reports a large LLM advantage

- **Source:** [R40: Muhammad et al., journal 2026](https://link.springer.com/article/10.1007/s41060-026-01201-x).
- **Locator:** Online publication date; §3.1 annotation; §§3.2–3.3 models;
  §4.1/Table 3 sentiment results; §4.2 return analysis.
- **Evidence:** Dataset contains 1,162 articles and 1,334 target cases for four
  companies, with news from September 2023 through January 2024. Table 3 reports
  DeepSeek-R1 macro F1 of 0.81 zero-shot and 0.87 five-shot, versus 0.66 for
  DeBERTa-v3-ABSA evaluated using fivefold cross-validation. Published online
  2 July 2026; the article cites an earlier 2025 conference version.
- **Inference:** Provides a concrete complementary result supporting LLM
  capability in a target-specific finance setting. Different results from R13
  are not contradictory because tasks, data, models, and supervision differ.
- **Limit:** Four companies, restricted full-text availability, several
  non-target-aware baselines, no strong sparse linear baseline, mixed serving
  interfaces/default settings, and no local reproduction. Annotation agreement
  concerns a shared subset, with most other cases individually labeled.
- **Consistency check:** Table 3 lists one-shot Llama 3 8B accuracy 0.52 and
  weighted recall 0.40. In standard single-label classification over the same
  examples/classes, weighted recall must equal accuracy. Clarification is
  needed before treating every table entry as internally verified.
- **Financial boundary:** Reported correlations concern contemporaneous returns,
  not proven future-return forecasting or trading profitability. Later model
  training is relevant to historical decision-simulation contamination.

## E15. Trustworthiness is a contextual system objective

- **Source:** [R41: NIST AI RMF 1.0, 2023](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/).
- **Locator:** Official section 3, AI Risks and Trustworthiness; official NIST
  publication landing page.
- **Evidence:** The framework discusses validity/reliability, safety,
  security/resilience, accountability/transparency, explainability/interpretability,
  privacy, and fairness, emphasizing contextual tradeoffs.
- **Inference:** A sentiment system should be selected under explicit quality
  and operating requirements, rather than accuracy alone.
- **Limit:** This is a voluntary general framework, not an empirical comparison
  or a prescription to choose classical NLP. Transparency alone does not prove
  correctness or fairness. The official HTML section was inspected, not a PDF.

## E16. Aspect-based sentiment applies to employee surveys

- **Source:** [R42: Rink et al., NLP4HR 2024](https://aclanthology.org/2024.nlp4hr-1.2/).
- **Locator:** Abstract and paper metadata.
- **Evidence:** Studies 1,458 Dutch open-ended survey responses, identifies six
  aspects, and proposes Dutch BERT-based few-shot approaches with bag-of-words
  and zero-shot comparisons.
- **Inference:** Survey analysis provides an industry application in which
  preserving aspect-specific opinions can be more useful than a single label.
- **Limit:** Only the abstract/metadata were inspected; no detailed ranking is
  inferred. This independently identified source is not assumed to be the
  unspecified survey reference [3] in the contributed draft.

## Claims deliberately not made

- That a particular 2026 LLM is the most accurate sentiment system.
- That every LLM beats every classical model, or that the reverse holds.
- That classical inference has zero cost, or that there is a fixed speed ratio.
- That the hypothetical $250 token example uses current provider prices.
- That a neutral sentiment label proves the absence of financial risk.
- That a model-generated rationale proves faithful interpretability.
- That a sentiment benchmark score demonstrates trading profitability.
- That any experiment in this repository has been executed.
