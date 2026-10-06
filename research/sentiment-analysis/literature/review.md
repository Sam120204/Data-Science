# Sentiment analysis: classical NLP, transformer classifiers, and prompted LLMs

Research date: 6 October 2026. Reference IDs link to the
[annotated bibliography](reading-list.md); evidence and qualifications appear in
the [evidence ledger](evidence-ledger.md).

Related analysis appears in [additional findings](additional-findings.md), with
draft provenance in the [archive](../archive/README.md).

## Contents

1. [Research question and conclusions](#1-the-answer-to-the-research-question)
2. [Task definition](#2-what-problem-does-sentiment-analysis-solve)
3. [Why sentiment is difficult](#3-why-is-the-problem-difficult)
4. [Existing method families](#4-existing-method-families-and-how-they-work)
5. [Comparative evidence](#5-what-the-comparative-literature-supports)
6. [Practical selection criteria](#6-why-classical-methods-can-still-be-the-right-choice-in-2026)
7. [Finance and industry applications](#7-why-this-matters-in-finance-and-industry)
8. [Fair evaluation](#8-how-to-compare-the-methods-fairly)
9. [Conclusions and open questions](#9-research-conclusions-and-open-questions)

## 1. The answer to the research question

**People still use classical NLP because the objective is to produce useful,
reliable sentiment measurements under operational constraints.** The most
capable general-purpose model is not automatically the best system for a
specific, repeated classification task.

For a stable label definition and a representative labeled dataset, word or
character n-grams with logistic regression or a linear SVM remain legitimate
baselines. Their advantages include inexpensive CPU inference, local execution,
direct feature contributions, and reproducible model artifacts. Whether those
advantages justify deployment depends on measured errors, not their age.
([R01](https://aclanthology.org/W02-1011/), [R03](https://aclanthology.org/P12-2018/), [R28](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction))

Prompted LLMs offer a different advantage: they can use a task definition and
examples without task-specific weight updates. This makes them useful for new
domains, exploratory analysis, complex extraction, and rapidly changing label
schemes. They also incur their own costs: model inference, prompt validation,
output parsing, version management, and quality checks. ([R13](https://aclanthology.org/2024.findings-naacl.246/), [R14](https://arxiv.org/abs/2304.04339), [R20](https://arxiv.org/abs/2310.11324))

The comparison should include a third family: **trained transformer classifiers**
such as BERT, RoBERTa, and FinBERT. These use contextual representations but
usually predict a fixed set of labels through a classification head. They often
provide a practical alternative between sparse linear models and prompted
generative models. SetFit, distillation, and hybrid pipelines further weaken a
simple two-way distinction. ([R10](https://aclanthology.org/N19-1423/), [R11](https://arxiv.org/abs/1910.01108), [R12](https://arxiv.org/abs/1908.10063), [R15](https://arxiv.org/abs/2209.11055))

There is no source-supported universal winner in 2026. Published comparisons
depend on the task, training labels, model versions, language, test distribution,
and evaluation procedure. A study of GPT-3.5-era models cannot establish the
relative accuracy of all current LLMs. It can still identify useful evaluation
questions and observed failure mechanisms. ([R13](https://aclanthology.org/2024.findings-naacl.246/))

## 2. What problem does sentiment analysis solve?

Sentiment analysis turns unstructured language into information about attitudes,
evaluations, or domain-specific favorable and unfavorable implications. A simple
task maps a review to positive, negative, or neutral. A richer task identifies
**who expresses which opinion about which target or aspect, with what polarity**.

For example, in “The app is easy to use, but its payment system is unreliable,”
a document label loses the useful distinction: usability is positive and payment
reliability is negative. Aspect-based sentiment analysis can preserve it. Some
tasks provide the aspect in advance; others require extracting the aspect, opinion
expression, and polarity together. Those are different prediction problems.
([R07](https://aclanthology.org/S14-2004/), [R13](https://aclanthology.org/2024.findings-naacl.246/))

The label must be defined before a model can be evaluated:

| Intended measurement | What a label means | Main ambiguity |
|---|---|---|
| Consumer evaluation | Approval or disapproval of a product/service | Different aspects can conflict |
| Emotional expression | The writer's emotional state | Anger, fear, joy, and sadness are richer than positive/negative |
| Investor stance | Bullish or bearish view toward a named asset | A view can be speculative rather than factual |
| Financial news sentiment | Favorable or unfavorable implication for a specified entity under a specified rubric | Time horizon, expectations, and affected entity matter |
| Document tone | Language expressing negativity, uncertainty, or other categories | Tone is different from realized economic outcomes |
| Subjectivity | Whether language expresses an opinion rather than a factual assertion | A factual event can still have an unfavorable economic implication |
| Sentiment intensity | Strength under a defined continuous or ordinal rubric | Scores from different resources are not automatically comparable |
| Proposition-level stance | Support or opposition toward a specified proposition | Opposition need not involve negative emotional language |

Emotion recognition, stance detection, sarcasm detection, and toxicity detection
are related tasks, but their labels are not interchangeable. A negative review
is not necessarily abusive, and “I fear this stock will rise before I can buy it”
contains fear alongside a bullish expectation. GoEmotions illustrates the richer
emotion taxonomy. ([R17](https://aclanthology.org/2020.acl-main.372/))

“Neutral,” “mixed,” and “insufficient information” should also be distinguished.
A text can express no sentiment, express opposing sentiments, or lack enough
context to determine the intended meaning. Collapsing them into neutral changes
what the system measures.

The unit of analysis also matters: a document, sentence, named target, and
aspect/opinion tuple require different labels and metrics. A polarity classifier
does not automatically provide a validated intensity score or subjectivity label.

## 3. Why is the problem difficult?

The root difficulty is that sentiment is a relation between language, context,
and a target. It is not an intrinsic property of individual words.

The following examples are **constructed illustrations**, not benchmark items or
tested model outputs:

| Example | Underlying difficulty |
|---|---|
| “The service was not good.” | Negation changes polarity; the scope matters |
| “Great, another outage.” | Surface-positive words can express sarcasm |
| “I waited forty minutes and nobody came.” | Negative sentiment is implied without an explicit sentiment adjective |
| “A won the contract; B lost it.” | Sentiment depends on the target entity |
| “The camera is excellent, but the battery is awful.” | Opposing sentiments belong to different aspects |
| “Losses narrowed from $10 million to $2 million.” | A negative accounting term occurs in an improving situation |
| “Profit increased, but missed the forecast.” | Absolute growth and performance relative to expectations differ |
| “The CEO called the results ‘excellent’; analysts disagreed.” | Opinion holder and attribution matter |

**Composition and context.** Bag-of-words loses word order. Bigrams can learn
“not good,” but cannot reliably represent arbitrary negation scope, quotation,
long-distance dependencies, or discourse. Neural contextual representations help
model these relationships, although learning them from data does not guarantee
robustness. ([R03](https://aclanthology.org/P12-2018/), [R08](https://aclanthology.org/D13-1170/), [R10](https://aclanthology.org/N19-1423/), [R18](https://aclanthology.org/2020.acl-main.442/))

**Domain dependence.** General sentiment dictionaries can assign inappropriate
polarity to routine financial vocabulary. Loughran and McDonald found that
almost three-fourths of the words flagged as negative by the Harvard dictionary
in their 1994–2008 10-K sample were words normally not negative in financial
contexts. This is a result about a particular dictionary and corpus, not the error
rate of every dictionary or classifier. ([R36](https://doi.org/10.1111/j.1540-6261.2010.01625.x))

**Distribution shift.** A model trained on product reviews may face financial
news, a different language variety, new slang, or a changed class balance.
Covariate shift concerns changes in inputs; label shift concerns class
proportions; concept shift concerns changes in the input-to-label relationship.
These can overlap. Changes in an annotation policy are another source of
measurement instability. An increase in unfamiliar terms signals possible shift,
but only labeled audits can establish whether predictive quality changed.
([R25](https://aclanthology.org/2025.findings-acl.441/); evaluation synthesis)

**Ambiguity in the labels themselves.** Annotators can disagree about sarcasm,
mixed opinions, and economic implications. Financial PhraseBank includes subsets
defined by annotator agreement. A model result on the unanimous subset is not
directly comparable to one on the broader, more ambiguous subset. ([R06](https://arxiv.org/abs/1307.5336), [R12](https://arxiv.org/abs/1908.10063))

**Shortcut learning and coverage.** A model can exploit vocabulary associated
with a class without learning the intended linguistic distinction. Aggregate
accuracy may conceal failures on negation or a language variety. CheckList
demonstrates why behavioral tests are useful alongside held-out benchmarks.
([R18](https://aclanthology.org/2020.acl-main.442/), [R25](https://aclanthology.org/2025.findings-acl.441/))

**Unstated financial context.** A sentence about rising interest rates can have
different implications for a borrower, a bank, a bondholder, and a currency.
Providing a target and horizon improves task definition; it does not resolve
missing economic facts. Sometimes abstention is the appropriate output.

## 4. Existing method families and how they work

### 4.1 Rules and sentiment lexicons

A lexicon assigns sentiment values or categories to words. A basic system
counts positive and negative terms, optionally normalizing by document length.
Rules can adjust for negation, intensifiers, punctuation, and contrastive clauses.

**VADER** combines a lexicon with rules tailored to social media expressions,
including capitalization, punctuation, degree modifiers, and negation. Its
compound score is a normalized sentiment score, not a calibrated probability
that the text belongs to a class. Thresholds converting scores into labels must
be specified. ([R04](https://ojs.aaai.org/index.php/ICWSM/article/view/14550), [R29](https://github.com/cjhutto/vaderSentiment))

**Loughran–McDonald** provides domain-specific financial word lists, including
negative, positive, uncertainty, litigious, constraining, and modal categories.
An uncertainty measure is not simply a negative sentiment measure. The word
lists and the formula used to aggregate them both form part of the operational
definition. ([R05](https://sraf.nd.edu/loughranmcdonald-master-dictionary/), [R36](https://doi.org/10.1111/j.1540-6261.2010.01625.x))

Turney's early approach estimates semantic orientation using associations of
phrases with positive and negative reference terms. This is a useful historical
example of sentiment inference without a supervised document classifier. ([R02](https://aclanthology.org/P02-1053/))

**SentiWordNet** scores WordNet synsets for positivity, negativity, and
objectivity/neutrality. It therefore distinguishes word senses rather than
assigning one score to every occurrence of a word. A system still needs to
identify the relevant sense and combine scores in context; the resource itself
does not resolve negation scope or target attribution.
([R38](https://aclanthology.org/L10-1531/))

Lexicons work well when transparency, a stable textual measure, or minimal
training resources matter. Their central limitation is coverage of context and
composition. Updating a dictionary can also break comparability with historical
measurements unless the version is fixed.

### 4.2 Bag-of-words / TF-IDF with supervised classifiers

The pipeline is:

1. Tokenize text into words, word n-grams, or character n-grams.
2. Convert each document into a sparse feature vector.
3. Learn the relationship between those features and labeled examples.
4. Apply the same transformation and classifier to new text.

**Bag-of-words** is a representation: it records counts or presence of tokens.
**TF-IDF** is a weighting scheme, not a classifier. It upweights terms frequent
in a document and downweights terms widespread across the training corpus.
One common smoothed inverse-document-frequency definition is
`idf(t) = log((1 + N)/(1 + df(t))) + 1`; normalization and term-frequency choices
vary by implementation. ([R28](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction))

Common classifiers include:

| Classifier | Mechanism | Useful property | Limitation |
|---|---|---|---|
| Multinomial Naive Bayes | Combine class priors and token likelihoods under a conditional-independence assumption | Fast training and inference; useful text baseline | Feature independence is unrealistic; confidence can be poor |
| Logistic regression | Learn a weighted sum of features; transform logits to class probabilities | Regularized, efficient; direct feature contributions | Sparse features have limited semantic generalization; probabilities still need validation |
| Linear SVM | Learn a separating boundary with a large margin | Strong sparse-text baseline | Decision scores are not calibrated probabilities |
| NB-SVM | Reweight features using Naive Bayes log-count ratios, then train a linear SVM | A strong, simple sentiment baseline | Still depends on observed lexical features |
| Tree ensembles | Combine decision trees over input features | Can mix text-derived and structured variables | Often a weaker default for very high-dimensional sparse text than linear methods |

For a linear classifier, `score = b + sum_j w_j x_j`. The term `w_j x_j`
gives the feature's contribution to that model score. This makes the decision
inspectable; it does not prove the word causes the writer's attitude or a market
outcome.

Wang and Manning showed that bigrams and classifier variants materially change
results. Their findings support using a strong classical baseline, not treating
one lightly tuned unigram model as representative of classical NLP. ([R03](https://aclanthology.org/P12-2018/))

Routine preprocessing can destroy useful signals. Removing “not,” stripping
emoji, or discarding punctuation can hurt sentiment analysis. Fit the vocabulary
and IDF weights on the training set only. Use regularization and validation rather
than assuming all stopwords should be removed. Character n-grams can help with
spelling variation, but do not solve sarcasm or long-range context.

### 4.3 Earlier neural models: CNNs and recurrent networks

Word embeddings represent tokens as dense vectors. A **CNN** applies filters
over local windows to detect predictive phrase patterns, then pools those features
for classification. Kim demonstrated a straightforward CNN sentence classifier
using pretrained embeddings. ([R09](https://aclanthology.org/D14-1181/))

**RNNs/LSTMs** process sequences and can model order; bidirectional versions use
both directions within the available text. Recursive models instead combine
representations along a syntactic tree. Socher and colleagues introduced the
Stanford Sentiment Treebank and a recursive model for compositional sentiment.
([R08](https://aclanthology.org/D13-1170/))

These approaches remain useful historical and experimental baselines. Their
tradeoffs include training complexity and reliance on the quality of embeddings
and labeled examples. Static embeddings assign the same initial vector to a word
across contexts; later contextual models improve on that limitation.

### 4.4 Fine-tuned transformer classifiers

**BERT** learns contextual token representations through large-scale pretraining.
For sentiment classification, a classification head maps a pooled sequence
representation to class logits. Supervised fine-tuning updates the head and
usually some or all of the encoder using labeled sentiment examples. ([R10](https://aclanthology.org/N19-1423/))

Self-attention lets a token's representation depend on other tokens, helping with
context and relationships. A classification head can produce all class scores in
one forward pass rather than generating a verbal answer token by token.

**FinBERT** adapts BERT to financial language and financial sentiment labels.
The Araci paper evaluates Financial PhraseBank and FiQA; the ProsusAI model card
describes further financial-domain training and financial sentiment fine-tuning.
“FinBERT” is used by multiple projects, so a reproducible comparison should name
the exact checkpoint, tokenizer, label mapping, and revision. ([R12](https://arxiv.org/abs/1908.10063), [R30](https://github.com/ProsusAI/finbert), [R34](https://huggingface.co/ProsusAI/finbert))

**DistilBERT** illustrates knowledge distillation: a smaller student learns from
a larger teacher alongside training objectives. The broader lesson is that
contextual modeling can be made cheaper; there is no need to equate every neural
sentiment system with a frontier generative LLM. ([R11](https://arxiv.org/abs/1910.01108))

**TinyBERT** extends this compression example through transformer distillation
at pretraining and task-specific stages. Its four-layer variant reports more
than 96.8% of its teacher BERT-Base's GLUE performance while being 7.5 times
smaller and 9.4 times faster at inference in the original evaluation.
DistilBERT's abstract reports 40% smaller size, 97% retained language-understanding
capability, and 60% faster operation. These are historical, configuration-specific
results, not guaranteed sentiment accuracy or speed on current hardware.
([R39](https://aclanthology.org/2020.findings-emnlp.372/), [R11](https://arxiv.org/abs/1910.01108))

Transformer classifiers can outperform lexical approaches when contextual
distinctions matter, but require representative task labels and appropriate
evaluation. Pretraining is not a guarantee against dialect bias, domain shift,
or brittle behavior on targeted linguistic tests. ([R18](https://aclanthology.org/2020.acl-main.442/), [R25](https://aclanthology.org/2025.findings-acl.441/), [R35](https://aclanthology.org/2026.dravidianlangtech-1.2/))

### 4.5 Prompted LLMs: zero-shot and few-shot classification

A generative LLM conditions on an instruction, input text, and optionally labeled
examples, then produces a label or structured answer.

**Zero-shot** means no labeled demonstrations for this task are supplied in the
prompt. **Few-shot in-context learning** means a small set of demonstrations is
included. Neither term implies that the model was never trained, or that its
pretraining never contained similar tasks. In-context learning generally does
not update model weights during the request. ([R13](https://aclanthology.org/2024.findings-naacl.246/), [R14](https://arxiv.org/abs/2304.04339))

The prompt should specify the target, the label definitions, the available
context, and an output schema. Structured decoding can constrain output shape;
it cannot establish semantic correctness. If label logits are accessible, a
system can score candidate labels directly, but verbalizer choices and
calibration still require evaluation.

LLMs can often infer unfamiliar paraphrases, use broader background knowledge,
and extract multiple opinion elements in one request. They are attractive for
limited-label tasks and changing schemas. Yet their performance can depend on
prompt wording, demonstration order, model version, and the exact evaluation
task. Longer explanations add inference cost and can introduce unsupported
reasoning. ([R13](https://aclanthology.org/2024.findings-naacl.246/), [R20](https://arxiv.org/abs/2310.11324), [R27](https://aclanthology.org/2026.acl-long.928/))

An explanation such as “negative because of weak demand” is a generated
justification, not automatically a faithful account of the model's internal
computation. The 2026 circuit-analysis paper investigates internal mechanisms
and interventions; that is a different form of evidence from a prose rationale.
([R27](https://aclanthology.org/2026.acl-long.928/))

### 4.6 Task-adapted LLMs, SetFit, distillation, and hybrids

**Task-adapted generative models** can be fine-tuned on financial instructions
and labels. Parameter-efficient methods such as LoRA update a small additional
set of parameters while keeping most original weights fixed. This changes the
tradeoff: the system is no longer only a general-purpose model used in one prompt.
Financial adaptation research and FinGPT illustrate this direction. ([R22](https://arxiv.org/abs/2306.06031), [R24](https://arxiv.org/abs/2401.14777))

**SetFit** fine-tunes a pretrained sentence transformer using contrastive text
pairs constructed from a small labeled set, then trains a classification head on
the resulting embeddings. It demonstrates that scarce labels do not force a
choice between a weak sparse classifier and a large prompted model. ([R15](https://arxiv.org/abs/2209.11055), [R32](https://github.com/huggingface/setfit))

**LLM-assisted labeling and distillation** use a larger model to generate candidate
labels or supervision for a smaller deployment model. Human checks remain
necessary: training on incorrect synthetic labels can reproduce teacher errors.

**A cascade** can route easy examples to a small classifier, ambiguous cases to
an LLM, and unresolved cases to people. Routing might use calibrated scores,
disagreement, an out-of-domain check, or task-specific rules. The combined
system must be evaluated: the LLM receives a deliberately difficult subset,
so its overall benchmark score will not predict its performance on routed cases.
These are design options, not locally verified findings.

## 5. What the comparative literature supports

| Source | What was investigated | Defensible takeaway | Qualification |
|---|---|---|---|
| Wang & Manning, 2012 ([R03](https://aclanthology.org/P12-2018/)) | NB/SVM variants and unigram/bigram sentiment features | Classical baselines can be much stronger than a casual implementation | Historical datasets and competitors; not a 2026 LLM comparison |
| Araci, 2019 ([R12](https://arxiv.org/abs/1908.10063)) | Financial-domain BERT and neural baselines | Domain-adapted contextual classification is a serious financial sentiment option | Baseline tuning was unequal; benchmark subsets and splits matter |
| Zhang et al., NAACL 2024 ([R13](https://aclanthology.org/2024.findings-naacl.246/)) | 13 tasks, 26 datasets; prompted LLMs versus trained T5 | LLMs were strong with limited examples; structured and nuanced tasks remained difficult | English only; older LLMs; T5 is a neural model, not a bag-of-words baseline |
| Srirag et al., ACL Findings 2025 ([R25](https://aclanthology.org/2025.findings-acl.441/)) | Sentiment/sarcasm across Australian, Indian, and British English | Language variety and cross-variety transfer deserve separate evaluation | National varieties simplify dialects; data and annotation coverage are limited |
| Teles & Figueiredo, 2025 preprint ([R26](https://arxiv.org/abs/2510.15929)) | Financial sentiment across several models and three datasets | Relative performance varied by dataset; useful material for auditing comparison design | Mixed model families; omitted strong linear baselines; label-description inconsistency |
| Li et al., ACL 2026 ([R27](https://aclanthology.org/2026.acl-long.928/)) | Sentiment circuits and prompt sensitivity in open-weight LLMs | Knowing sentiment internally and reliably eliciting it can be different problems | Specific models, binary-filtered datasets, available sparse autoencoders |
| Muhammad et al., journal 2026 ([R40](https://link.springer.com/article/10.1007/s41060-026-01201-x)) | Target-aware Bloomberg financial sentiment; zero/few-shot generative models and lexical/encoder baselines | Strong reported LLM performance on an explicitly target-specific financial task | Four companies; access-restricted article text; baseline task differences; reporting consistency issue |

Two concrete findings from R13 illustrate why task definition matters. In its
Table 1, ChatGPT scores **94.20** on IMDb classification versus **93.93** for the
fully trained T5 reference, while restaurant-2014 unified aspect extraction
scores are **54.46** versus **75.31**. IMDb uses accuracy; the structured task
uses extraction F1. These numbers compare models **within each task**, and must
not be averaged into a universal sentiment accuracy or presented as current
2026 model results. These evaluations use 500 sampled test items per dataset;
the small IMDb difference is not evidence of statistically superior performance.
([R13](https://aclanthology.org/2024.findings-naacl.246/), Table 1 and Appendix Table 4)

Recent evidence also needs scrutiny. R26's “LLM” group includes DeBERTa and
XLM-RoBERTa classifiers, its classical baselines omit logistic regression and
LinearSVC, and preprocessing uses stopword removal and SVD. Its text gives two
inconsistent mappings for the financial-news numeric labels. These observations
limit reproducibility and the scope of its conclusions; they do not prove that
every reported score is wrong. ([R26](https://arxiv.org/abs/2510.15929), §§3.2–3.3)

R35 reports XLM-R accuracy of 99.7% on its Hinglish test set and 42.5% on a
400-example adversarial set. This is a targeted robustness warning, not a
population failure-rate estimate. The paper also describes 25% as chance for a
three-class problem, which is incorrect for uniform guessing (33.3%). Its
limitations acknowledge the small diagnostic set and absence of formal
significance testing. Treat this source as supplementary evidence, not a decisive
ranking. ([R35](https://aclanthology.org/2026.dravidianlangtech-1.2/), Tables 1–3 and Limitations)

A complementary financial result appears in Muhammad et al.'s journal version,
published 2 July 2026 with an earlier 2025 conference version. The dataset has
1,162 articles and 1,334 target-specific annotation cases involving four
companies. Table 3 reports five-shot DeepSeek-R1 macro F1 of **0.87**, compared
with **0.66** for its target/aspect DeBERTa baseline. This supports LLM capability
in that setting, while the paper's non-target-aware baselines, mixed serving
interfaces, restricted data access, and an inconsistent accuracy/weighted-recall
entry limit a broad conclusion. Its return correlations are contemporaneous,
not evidence of future-return profitability. See the
[addendum](additional-findings.md) and evidence entry E14 for the complete
qualifications. ([R40](https://link.springer.com/article/10.1007/s41060-026-01201-x), §§3–4)

## 6. Why classical methods can still be the right choice in 2026

| Consideration | Classical / compact classifier advantage | When an LLM can justify its extra complexity |
|---|---|---|
| Prediction volume | Small per-example compute for repeated fixed-label tasks | Errors are costly enough that better measured quality outweighs inference cost |
| Latency | Sparse linear inference avoids a large forward pass and answer generation | The application tolerates latency or benefits from richer extraction |
| Local execution | CPU deployment can be straightforward | A suitable local LLM and serving setup fit the requirements |
| Interpretability | Lexicon counts and linear feature contributions can be directly inspected | Validated evidence extraction or specialized mechanistic analysis adds value |
| Reproducibility | Frozen preprocessing, weights, and software define a stable artifact | A pinned LLM, prompt, and serving configuration can be maintained and audited |
| Annotation resources | Existing labels can make supervised training economical | Useful labels are scarce and the task can be described well |
| Task flexibility | A fixed classification contract is easy to operate | New aspects, entities, or label rubrics change frequently |
| Semantic complexity | Lexical patterns may be sufficient in a narrow domain | Context, paraphrase, or structured opinion extraction improves materially |

These are conditional engineering expectations. There is no measured “100 times
cheaper” or fixed latency ratio in this review. Hardware, document length,
batching, quantization, caching, serving overhead, and model size can change the
comparison. An open-weight LLM has compute and operational costs even without
per-token API charges.

The voluntary NIST AI Risk Management Framework provides a useful broader
objective: validity/reliability, transparency, explainability, privacy, and
fairness must be assessed in context. It does not recommend a particular model
family. Inspectable lexical features can aid debugging, but a transparent model
can still learn biased labels; local execution is available to both small
classifiers and suitably hosted LLMs. These properties belong to the deployed
system rather than following automatically from a model-family name.
([R41](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/))

Evaluate **total cost**, not only the bill for predictions:

`total cost = labeling + development + training + inference + monitoring + error handling`

For an API model, a simplified inference estimate is:

`N × ((input_tokens × input_rate + output_tokens × output_rate) / 1,000,000)`

Here rates are dollars per million tokens. As a **hypothetical arithmetic example**,
one million texts averaging 200 input tokens and 10 output tokens, at invented
rates of $1/million input tokens and $5/million output tokens, cost **$250** in
token charges. These are not provider prices. The example omits retries, cached
pricing, longer prompts, overhead, and error costs. Classical serving also has
costs and needs measurement. It would be invalid to compare $250 to an assumed
zero-cost CPU system.

For reliability, record model and prompt versions and test repeated predictions.
Low or zero decoding temperature does not universally guarantee identical
outputs. A fixed small classifier is easier to freeze, but it can still have
software/version differences and still needs drift monitoring.

## 7. Why this matters in finance and industry

**Finance: scalable measurement.** Earnings calls, filings, analyst reports,
news, and investor posts contain information that cannot be manually reviewed
at scale. Sentiment systems can support research triage, risk monitoring,
document comparison, and entity-specific news analytics. Financial sentiment
benchmarks explicitly include microblogs and news. ([R23](https://aclanthology.org/S17-2089/))

**Finance: domain validity.** The Loughran–McDonald result shows why using a
generic word list can measure the wrong thing. A rise in uncertain language is
different from worsening earnings. A claim about positive tone is different from
a claim about positive future returns. ([R05](https://sraf.nd.edu/loughranmcdonald-master-dictionary/), [R36](https://doi.org/10.1111/j.1540-6261.2010.01625.x))

**Finance: sentiment is not trading performance.** Tetlock reports relationships
between media pessimism, market prices, and trading volume in a historical
setting. This motivates research, but neither that result nor accurate sentiment
classification proves a profitable contemporary strategy. ([R37](https://doi.org/10.1111/j.1540-6261.2007.01232.x))

A trading study must separately consider public-information timing, market
expectations, horizon, transaction costs, liquidity, survivorship bias, and
out-of-sample performance. Historical LLM backtests need special care if model
training postdates the events: later factual knowledge can contaminate a
historical decision simulation. Restricting supplied context helps, but does not
prove absence of memorized future information.

**Industry: operational decisions.** Customer support can route complaints;
product teams can aggregate aspect-specific feedback; organizations can monitor
reputation. An overall sentiment average may conceal a payment failure affecting
a minority of users. False alarms, missed urgent complaints, and unequal errors
across customer language varieties are consequential deployment outcomes.

Open-ended employee surveys provide another application. Rink et al. study
aspect-based sentiment in 1,458 Dutch survey responses, including salary,
scheduling, communication, and personal attention. A whole-response label can
conceal opposing evaluations of these aspects. The study is an application
example for contextual classifiers, not evidence that prompted generative LLMs
always outperform other methods on surveys.
([R42](https://aclanthology.org/2024.nlp4hr-1.2/))

## 8. How to compare the methods fairly

The [evaluation protocol](../methodology/evaluation-protocol.md) provides the complete design.
Its essential principles are:

1. Define the same targets, labels, context, and abstention policy for every model.
2. Compare a lexicon, strong sparse linear baselines, a contextual classifier,
   and prompted LLMs on identical test examples.
3. Separate full-label, limited-label, and cross-domain comparisons. They answer
   different questions and have different resource budgets.
4. Keep the test set out of vectorizer fitting, prompt selection, example
   retrieval, calibration, and hyperparameter tuning.
5. Report macro F1, per-class errors, uncertainty, and behavioral slices alongside
   accuracy. Use extraction metrics for extraction tasks rather than reusing
   classification accuracy.
6. Measure cost, throughput, end-to-end latency, output validity, and repeatability.
7. Evaluate a recent or shifted-domain holdout before making deployment claims.

Confidence is another measurement problem. A softmax output can be
miscalibrated; an SVM margin is not a probability; an LLM's self-reported
“95% confidence” is not validated calibration. If confidence controls escalation,
fit and assess calibration on appropriate held-out data and measure performance
at each coverage level. ([R19](https://arxiv.org/abs/1706.04599))

## 9. Research conclusions and open questions

The evidence supports choosing the **smallest system that satisfies a validated
quality and operational requirement**, while preserving an escalation path for
cases it cannot handle. That recommendation is synthesis, not a theorem that
smaller models always win.

Classical NLP remains useful because stable tasks can reward efficiency,
inspectable decision rules, local control, and repeatable measurements. LLMs are
useful because broad pretraining and instructions can reduce dependence on
task-specific labels and support richer analysis. Fine-tuned encoders, SetFit,
and hybrid systems are essential alternatives in that decision.

The most valuable unanswered questions for a concrete project are:

- How much does a current prompted LLM improve over a well-tuned FinBERT or
  sparse linear baseline on recent, entity-specific financial text?
- Which error slices account for that improvement: negation, implied sentiment,
  expectations, mixed aspects, dialect, or attribution?
- At what traffic volume and error cost does one system become preferable?
- Does the improvement survive domain shift and new annotation rules?
- Can a validated cascade capture most of the benefit at lower total cost?

Answering those questions requires a controlled evaluation on the intended data.
This review establishes the methods and evidence needed to design it; it does
not substitute literature results for an experiment that has not been run.
