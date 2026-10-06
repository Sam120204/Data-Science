# Sentiment analysis: classical NLP, transformers, and LLMs

**Research question: Why choose classical sentiment analysis in 2026 when an
LLM can classify text through a prompt?**

This review explains the problem, why it remains difficult, how existing methods
address it, and the conditions that make each method useful. Paper links support
the findings; full citations and PDFs are in [References](REFERENCES.md).
Published results and engineering recommendations are distinguished from the
local example runs.

**Current progress:** The literature synthesis and baseline implementations are
complete for the current scope, with constructed-example execution checks.
Representative-data comparisons and operating-cost measurements remain pending.
The findings below guide those experiments; execution details are in
[Experiments](EXPERIMENTS.md).

## Contents

1. [Answer to the research question](#1-the-answer-to-the-research-question)
2. [What sentiment analysis solves](#2-what-problem-does-sentiment-analysis-solve)
3. [Root causes of difficulty](#3-why-is-the-problem-difficult)
4. [How the methods work](#4-existing-method-families-and-how-they-work)
5. [What the papers support](#5-what-the-comparative-literature-supports)
6. [Reasons to choose classical NLP](#6-why-classical-methods-can-still-be-the-right-choice-in-2026)
7. [Where classical methods remain useful](#7-where-classical-methods-remain-useful-in-practice)
8. [Deciding whether an LLM is worth the cost](#8-how-to-decide-whether-an-llm-is-worth-the-additional-cost)
9. [Conclusions and open questions](#9-research-conclusions-and-open-questions)

## 1. The answer to the research question

**Classical sentiment analysis remains useful when it delivers adequate quality
with lower total cost, predictable latency, and inspectable decisions.** This is
most plausible for a stable, repeated task with representative training labels
or a well-defined dictionary-based measure. It is a conditional model-selection
argument that must be tested on the intended data.
([R01](https://aclanthology.org/W02-1011/), [R03](https://aclanthology.org/P12-2018/),
[R28](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction))

Here, **classical NLP** includes lexicons/rules such as VADER and sparse
classifiers such as TF-IDF + logistic regression. **Fine-tuned transformer
classifiers**, including FinBERT, form a separate contextual alternative.
**Prompted LLMs** interpret instructions and generate labels or richer outputs.
Compact encoders, SetFit, and hybrid systems make the choice broader than a
simple classical-versus-LLM contest.
([R10](https://aclanthology.org/N19-1423/), [R11](https://arxiv.org/abs/1910.01108),
[R12](https://arxiv.org/abs/1908.10063), [R15](https://arxiv.org/abs/2209.11055))

**“One prompt” reduces the work needed to start classification.** It does not
establish that the labels measure the intended concept, that predictions remain
reliable on new language, or that serving the model is economical at the required
volume. LLMs can reduce dependence on task-specific training labels, particularly
for new or complex tasks, but representative human-labeled evaluation examples
are still needed to validate them. Prompt selection, output checks, model
versioning, and monitoring also require work.
([R13](https://aclanthology.org/2024.findings-naacl.246/),
[R14](https://arxiv.org/abs/2304.04339), [R20](https://arxiv.org/abs/2310.11324))

The question therefore becomes: **when does an LLM improve important errors
enough to justify the total cost and complexity of using it?** Older studies help
explain the tradeoffs, but cannot rank every current model. This review does not
establish a universal winner in 2026.

## 2. What problem does sentiment analysis solve?

Sentiment analysis converts large amounts of unstructured text into consistent
measurements of attitudes, evaluations, or favorable/unfavorable implications.
These measurements help people summarize feedback, track document tone, or
identify news that deserves attention. The useful output depends on what is
being measured and toward whom.

For example, “The app is easy to use, but its payment system is unreliable”
contains positive sentiment about usability and negative sentiment about
payments. A single document label loses that distinction. Aspect-based analysis
preserves it; some tasks supply the aspect, while others require extracting both
the aspect and its sentiment.
([R07](https://aclanthology.org/S14-2004/),
[R13](https://aclanthology.org/2024.findings-naacl.246/))

Define the target and label meaning before comparing models:

| Task | What the output should measure | Why this affects model choice |
|---|---|---|
| Whole-review polarity | Overall approval or disapproval | A fixed-label sparse classifier may be sufficient. |
| Aspect or company-specific sentiment | An evaluation toward a named aspect/entity | Word counts alone can miss who benefits or suffers. |
| Financial document tone | Negative, uncertain, or other specified language categories | A fixed domain dictionary can provide an inspectable measure. |
| Investor stance or financial implications | Bullish/bearish views or implications under a defined horizon | Context and expectations may matter more than emotional wording. |

Emotion, subjectivity, stance, and intensity are related measurements with their
own definitions. Fear does not always imply a bearish view; a factual sentence
can describe an unfavorable event without expressing an opinion. A positive/
negative classifier does not automatically validate these other outputs.
([R17](https://aclanthology.org/2020.acl-main.372/))

Likewise, **neutral**, **mixed**, and **insufficient information** describe
different situations. Collapsing them changes the task. A more powerful model
cannot compensate for an unclear label policy: models may disagree because they
are answering different questions. Classical NLP is most defensible when its
output matches a clear, stable measurement need.

## 3. Why is the problem difficult?

**The root difficulty is that sentiment depends on meaning, context, and a
target.** Individual words provide clues, but their polarity can change when
combined with other words or interpreted in another domain. The examples below
are constructed illustrations, not tested model outputs.

| Example | Root cause of the difficulty |
|---|---|
| “The service was not good.” | Negation changes the evaluation; its scope must be identified. |
| “Great, another outage.” | Sarcasm creates a gap between literal wording and intended meaning. |
| “I waited forty minutes and nobody came.” | The complaint is implied through an event rather than a sentiment adjective. |
| “A won the contract; B lost it.” | The same event has different implications for different targets. |
| “The camera is excellent, but the battery is awful.” | Different aspects carry conflicting evaluations. |
| “Losses narrowed from $10 million to $2 million.” | A negative accounting term appears in an improving situation. |
| “Profit increased, but missed the forecast.” | The evaluation depends on expectations as well as absolute change. |
| “The CEO called the results ‘excellent’; analysts disagreed.” | Opinions must be assigned to the correct speakers. |

**Context and composition.** Bag-of-words discards word order. Bigrams can learn
“not good,” but do not capture arbitrary negation scope, quotations, or distant
relationships. Contextual models learn richer representations, yet can still
misread sarcasm or missing context. A target and horizon clarify a financial
question; they do not supply economic facts absent from the text.
([R03](https://aclanthology.org/P12-2018/), [R08](https://aclanthology.org/D13-1170/),
[R10](https://aclanthology.org/N19-1423/), [R18](https://aclanthology.org/2020.acl-main.442/))

**Domain dependence.** The meaning associated with vocabulary differs across
applications. Loughran and McDonald found that almost three-fourths of the words
flagged as negative by the Harvard dictionary in their 1994–2008 10-K sample
were ordinarily not negative in financial usage. This concerns flagged words in
one corpus, rather than a document-level error rate. It explains why a financial
dictionary or domain-adapted model can be more appropriate than a generic one.
([R36](https://doi.org/10.1111/j.1540-6261.2010.01625.x))

**Why drift happens—and why it is hard to detect.** A deployed model learns or
uses patterns that may become less useful as the text, audience, or task changes:

| What changes | Example | What it means for evaluation |
|---|---|---|
| Inputs | New slang, products, or language varieties | Familiar training patterns may no longer cover the workload. |
| Class proportions | A real service outage creates more negative feedback | More negative predictions may reflect real events rather than worse predictions. |
| Input-to-label relationship | A word gains a new meaning in the community | Previously useful associations can become misleading. |

These changes can overlap. Changing the annotation policy is another source of
instability. Monitoring vocabulary, predicted labels, or confidence can flag a
possible change, but cannot by itself establish an increase in mistakes: current
true labels are usually unavailable, and a model can remain confident while
being wrong. Audit a representative, newly labeled sample and compare errors
across classes and user groups. Drift can affect both classical models and LLMs;
broad pretraining does not guarantee reliable adaptation.
([R25](https://aclanthology.org/2025.findings-acl.441/); monitoring recommendations
are evaluation synthesis.)

**Ambiguous labels and shortcuts.** Annotators can disagree about mixed opinions
or sarcasm, so evaluation also depends on label reliability. Financial PhraseBank
has subsets with different levels of annotator agreement; their results are not
interchangeable. Agreement is informative, rather than a strict mathematical
ceiling on accuracy against adjudicated labels. Models can also learn shortcuts,
such as associating a brand with a sentiment class, that fail on new inputs.
High aggregate accuracy may conceal these errors.
([R06](https://arxiv.org/abs/1307.5336), [R12](https://arxiv.org/abs/1908.10063),
[R18](https://aclanthology.org/2020.acl-main.442/))

These difficulties explain the tradeoff: classical methods can be sufficient
when validated lexical patterns match a stable task. Contextual classifiers or
LLMs become more valuable when context-dependent errors matter. Every family
still needs a clear task definition and checks on current, relevant examples.

## 4. Existing method families and how they work

**All these methods belong to NLP; LLMs are one type of NLP model.** For this
research question, the useful distinction is between classical methods,
neural classifiers, and generative LLMs used through prompting or adaptation.

| Section and methods | Category used in this review |
|---|---|
| **4.1:** VADER, financial dictionaries, SentiWordNet | Classical NLP: lexicons and rules |
| **4.2:** Bag-of-words/TF-IDF + Naive Bayes, logistic regression, SVM | Classical NLP: statistical classifiers |
| **4.3:** CNNs, RNNs/LSTMs, recursive models | Earlier neural NLP |
| **4.4:** BERT, FinBERT, DistilBERT, TinyBERT classifiers | Contextual transformer classifiers |
| **4.5:** Zero-shot and few-shot prompting | Prompted generative LLMs |
| **4.6:** Adapted LLMs, SetFit, distillation, cascades | Mixed approaches: LLM adaptation, encoder training, or combinations of models |

Transformer classifiers learn contextual representations and predict fixed
labels; prompted LLMs generate an answer from instructions. Both use neural
models, but their deployment and training requirements differ. In section 4.6,
SetFit is encoder-based, while labeling, distillation, and cascades can combine
larger models with smaller classifiers.

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
measurements unless the version is fixed. For a task that explicitly measures
word-based tone, a fixed lexicon can be a suitable output definition; richer
company-specific interpretation requires separate validation.

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
spelling variation, but do not solve sarcasm or long-range context. This makes
sparse models strong candidates for repeated, fixed-label tasks with useful
training data, while complex contextual distinctions can justify another model.

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
The original comparison explored BERT more thoroughly than its neural
baselines and found modest differences among additional domain-pretraining
choices. Its gains should not all be attributed solely to domain pretraining.
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

**Main limitations:** Fine-tuning needs representative labeled examples; a model
trained on reviews can misread financial news, and changing domains or label
definitions may require new labels and retraining. Compared with VADER or sparse
linear models, transformer classifiers usually need more memory and inference
compute, and their individual decisions are harder to explain. Input-length
limits can truncate relevant evidence in long documents. They can still fail on
sarcasm, dialect variation, and unfamiliar language. Compression helps with
compute demands, but domain shift and robustness still need evaluation.
([R10](https://aclanthology.org/N19-1423/), [R18](https://aclanthology.org/2020.acl-main.442/), [R25](https://aclanthology.org/2025.findings-acl.441/))
For model selection, an encoder is worth testing when sparse features miss
important context but the application still needs a fixed set of sentiment labels.

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
computation. The 2026 circuit-analysis paper investigates Gemma-2-2B and Llama-3.1-8B
across seven datasets, using available sparse autoencoders and binary-filtered
transfer data. It studies internal mechanisms and interventions; that is a different form of evidence from a prose rationale.
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

The studies suggest several useful patterns. Their results depend on the task,
training data, and model version, so they do not establish one universal winner.

The papers supporting this section are listed below. Full titles, author lists,
and available PDF links are in [References](REFERENCES.md).

| Paper | What it contributes |
|---|---|
| [Wang & Manning (2012; R03)](https://aclanthology.org/P12-2018/) | Shows why carefully built classical baselines deserve consideration. |
| [Araci (2019; R12)](https://arxiv.org/abs/1908.10063) | Evaluates FinBERT for financial sentiment classification. |
| [Zhang et al. (2024; R13)](https://aclanthology.org/2024.findings-naacl.246/) | Finds that LLM performance depends on the task and available labels; uses older models. |
| [Srirag et al. (2025; R25)](https://aclanthology.org/2025.findings-acl.441/) | Examines sentiment and sarcasm across English varieties. |
| [Teles & Figueiredo (2025; R26)](https://arxiv.org/abs/2510.15929) | Compares financial sentiment models across datasets; baseline and label-description limitations require caution. |
| [Li et al. (2026; R27)](https://aclanthology.org/2026.acl-long.928/) | Investigates why different prompts can elicit different sentiment predictions. |
| [Rahul & Adebayo (2026; R35)](https://aclanthology.org/2026.dravidianlangtech-1.2/) | Shows weaker performance on difficult examples in a small Hinglish robustness study. |
| [Muhammad et al. (2026; R40)](https://link.springer.com/article/10.1007/s41060-026-01201-x) | Reports strong LLM results for company-specific financial sentiment, with limited coverage and comparison issues. |

**Classical methods remain serious baselines.** Wang and Manning showed that
simple word-based classifiers can perform strongly when their features and
training are chosen carefully. This supports comparing LLMs against a well-built
classical model. The study predates current LLMs, so it cannot establish which
family is better today. ([R03](https://aclanthology.org/P12-2018/))

**Fine-tuned transformers offer a useful middle option.** FinBERT shows how
contextual models trained for financial language can improve sentiment
classification. Its results support including a financial transformer in the
comparison, although the original study explored BERT more thoroughly than its
other neural baselines. ([R12](https://arxiv.org/abs/1908.10063))

**LLMs can perform well, but the task matters.** In Zhang et al.'s study, ChatGPT
and a trained T5 model achieved similar movie-review accuracy: **94.20% and
93.93%**. For the more detailed task of extracting which aspects were praised or
criticized, trained T5 performed better. LLMs were particularly useful when few
labeled examples were available. This English-language study used older LLMs;
it does not rank today's models. ([R13](https://aclanthology.org/2024.findings-naacl.246/))

**Financial results are promising, with important limits.** A study of 1,162
Bloomberg articles about four companies reported the following results for
sentiment toward named companies:

| Method | Reported macro F1 |
|---|---:|
| VADER | 0.37 |
| FinBERT | 0.54 |
| DeepSeek-R1, prompted with five labeled examples | 0.87 |

Macro F1 combines precision and recall while giving each sentiment class equal
weight; higher is better. The LLM scored strongly in this setting, but several
baselines were not designed for company-specific sentiment, and strong sparse
linear classifiers were omitted. Full article text has restricted access, and
some table entries need clarification. These are published results, not local
measurements or evidence of trading profitability.
([R40](https://link.springer.com/article/10.1007/s41060-026-01201-x))

**High scores still need checks in realistic conditions.** Research on English
varieties and prompt sensitivity shows that language differences and instruction
wording can change results. Test the language, domain, and inputs the system
will actually face. ([R25](https://aclanthology.org/2025.findings-acl.441/),
[R27](https://aclanthology.org/2026.acl-long.928/))
A small Hinglish study also found weaker performance on difficult examples,
supporting the need to check robustness beyond ordinary benchmark scores.
([R35](https://aclanthology.org/2026.dravidianlangtech-1.2/))

The conclusion is that classical models, fine-tuned transformers, and prompted
LLMs all deserve consideration. Classical models remain useful when efficiency
and stable labels matter; transformers and LLMs can justify additional cost when
they reduce important errors. Choose using the same relevant test data and
measured cost and latency, rather than model age or one published score.

## 6. Why classical methods can still be the right choice in 2026

The strongest case for classical NLP is a **validated, stable task where its
errors are acceptable and its operating advantages matter**. Convenience at
setup and suitability at deployment are separate considerations.

| Reason to choose classical NLP | Why the advantage can exist | When a richer model may be preferable |
|---|---|---|
| Low inference cost at high volume | Sparse classifiers score active features; lexicons apply small rule sets. | Better contextual predictions reduce sufficiently important errors. |
| Predictable latency | Small local models avoid large-model inference and generated explanations. | The application tolerates the measured delay for useful extra capability. |
| Inspectable decisions | Dictionary matches and linear feature contributions can be examined directly. | Contextual interpretation is essential and explanations can be validated appropriately. |
| Consistent measurements | Frozen dictionaries, preprocessing, and weights define a stable artifact. | The measurement requires flexible aspects, targets, or changing schemas. |
| Existing training labels | Supervised fitting can reuse representative labeled examples. | Labels are scarce and a prompted model performs well with limited demonstrations. |
| Simple local deployment | Many classical models operate on ordinary CPUs with modest memory needs. | A local encoder or LLM fits the resources and provides valuable improvements. |

These are engineering expectations, rather than measured universal speed or cost
ratios. FinBERT and compressed encoders may also meet deployment constraints.
LLMs can run locally; privacy and reproducibility depend on the actual system.
A transparent model can still learn biased or spurious associations. NIST's
voluntary framework likewise treats reliability, explainability, privacy, and
fairness as contextual requirements.
([R41](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/))

**The cost advantage depends on the workload.** Training a sparse classifier
requires labels and development effort, which can be spread over many repeated
predictions. An LLM can reduce that initial adaptation work, but each request
still consumes compute; examples, context, explanations, and retries also add
tokens or processing. Count the complete lifecycle:

`total cost = labeling + development + training + inference + monitoring + error handling`

Measure actual hardware or API cost, document length, batching, and request
latency. Open-weight models and CPU baselines both have operating costs. There
is no justified break-even traffic volume until those quantities are measured.

**Reliability requires maintenance in every family.** Pin model, software, and
prompt versions, test repeated outputs, and audit drift. Low decoding temperature
does not universally guarantee identical LLM responses. A stable artifact makes
comparison easier, but cannot prevent changes in the language it receives.

## 7. Where classical methods remain useful in practice

Applications help answer the research question by showing which properties
matter. The following selection arguments are based on the methods and cited
studies; they are not locally measured deployment outcomes.

**Repeated feedback classification.** A team processing many short comments
under fixed positive/negative/neutral labels may already have useful training
examples. TF-IDF + a linear classifier is a credible candidate if it meets the
required quality and response time. The practical question is whether a richer
model reduces important missed complaints enough to justify its additional
cost. Strong classical baseline design matters to this comparison.
([R03](https://aclanthology.org/P12-2018/))

**Consistent financial-tone measurement.** If the goal is to count negative or
uncertain financial language consistently across filings, a fixed
Loughran–McDonald dictionary can provide an inspectable measure. Domain vocabulary
matters: uncertainty and negative tone are distinct categories. A task asking
which company benefits from an event requires additional contextual interpretation
and a separate evaluation.
([R05](https://sraf.nd.edu/loughranmcdonald-master-dictionary/),
[R36](https://doi.org/10.1111/j.1540-6261.2010.01625.x))

**When richer analysis earns its cost.** News about multiple companies and
feedback about several aspects may require preserving conflicting evaluations.
Financial sentiment benchmarks and the target-specific study in section 5
illustrate these tasks. The Dutch employee-survey study also shows why salary,
scheduling, and communication can need separate labels. Target-aware classifiers
or LLMs deserve consideration when these distinctions materially improve the
useful output; a single cheap label can discard what the application needs.
([R23](https://aclanthology.org/S17-2089/),
[R40](https://link.springer.com/article/10.1007/s41060-026-01201-x),
[R42](https://aclanthology.org/2024.nlp4hr-1.2/))

**A downstream benefit needs its own evidence.** Sentiment and stock returns
can move together because the same earnings surprise influences both, or because
price movements shape subsequent news language. This makes correlation alone
insufficient to establish causation or future-return prediction. Historical
associations motivate research, but better sentiment accuracy does not establish
trading profitability. An expensive model is justified by demonstrated value for
the intended decision, not by assuming a sentiment score causes that value.
([R37](https://doi.org/10.1111/j.1540-6261.2007.01232.x))

## 8. How to decide whether an LLM is worth the additional cost

The comparison should establish whether additional model capability produces
useful gains under the application's requirements. The detailed protocol is in
[Experiments](EXPERIMENTS.md); the decision rests on four checks:

1. **Compare the same task.** Give models the same permitted context, targets,
   labels, and test items. Include a strong sparse baseline, an appropriate
   contextual classifier, and a prompted LLM. State which training labels and
   prompt examples each receives; full-label and limited-label settings answer
   different questions.
2. **Find the errors that matter.** Report per-class mistakes and macro F1,
   which balances precision and recall across classes. Check negation, mixed
   targets, implied sentiment, and relevant language varieties. When mistakes
   have different consequences, evaluate those consequences alongside scores.
3. **Measure the full operating tradeoff.** Include labeling, adaptation,
   inference, retries, monitoring, and human review. Measure latency and
   throughput on the intended workload. A gain in average accuracy may have
   little value if it misses urgent complaints or exceeds the response-time
   requirement.
4. **Check that the result survives new data.** Reserve untouched test examples;
   keep test labels out of feature fitting, tuning, and prompt selection. Audit
   possible pretrained-model exposure to the benchmark, and test a recent or
   shifted-domain sample. Report uncertainty, since a small observed score
   difference may be sampling noise.

If confidence controls escalation to an LLM or a person, validate it on held-out
labels. An SVM margin or a model's verbal “95% confidence” is not an established
probability of correctness, and confidence can become unreliable under drift.
([R19](https://arxiv.org/abs/1706.04599))

Choose classical NLP when it meets the necessary quality and operating
requirements at lower measured total cost. Choose a contextual model, LLM, or
hybrid when it delivers enough additional value to justify its costs. Successful
classification in one prompt is a starting point; evidence from this comparison
is what supports a deployment decision.

## 9. Research conclusions and open questions

**Classical sentiment analysis remains relevant because a stable, clearly
defined task can reward efficient computation, inspectable decisions, and
repeatable measurements.** These advantages matter only when the method measures
the intended sentiment and handles important errors adequately. They do not
make classical NLP universally more accurate or easier to maintain.

LLMs are attractive when instructions and broad contextual knowledge help with
scarce labels or richer outputs. Fine-tuned and compact transformer classifiers
provide another option. All families face ambiguous labels, domain-dependent
meaning, and changing data, so selecting a capable model is only part of building
a reliable sentiment system.

The remaining questions require measurements on the intended data:

- Which contextual errors does a current LLM reduce compared with a strong sparse
  classifier and a suitable financial encoder?
- How do available labels, prediction volume, and the consequences of mistakes
  change the total-cost comparison?
- Do the benefits survive recent text, domain changes, and different user groups?
- Can selective escalation preserve useful gains while reducing operating cost?

The literature supports this decision framework rather than a universal 2026
ranking. The [implemented code and example checks](EXPERIMENTS.md) demonstrate
progress, but representative-data benchmarking and LLM execution remain pending.
The answer for a deployment must come from a clear task, trustworthy evaluation,
and measured quality and operating requirements.
