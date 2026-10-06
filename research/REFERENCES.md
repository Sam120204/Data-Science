# Annotated papers and primary resources

Research/access date: **6 October 2026**. Entries include authors, publication
dates, primary paper links, available PDFs, and review notes.

Suggested starting papers: **R03, R12, R13, R25, R27, and R40**.
Findings and qualifications are integrated in [Research](RESEARCH.md).
Implementation resources R28–R34 and dataset links appear at the end of this
document. Papers remain hosted by their publishers; direct PDFs are linked
where available.

<a id="r01"></a>
## R01: Thumbs up? Sentiment Classification using Machine Learning Techniques

- **Authors:** Bo Pang; Lillian Lee; Shivakumar Vaithyanathan.
- **Source date:** 2002/7.
- **Source:** [R01 primary page](https://aclanthology.org/W02-1011/) · [PDF](https://aclanthology.org/W02-1011.pdf).

Foundational supervised sentiment classification: compares machine-learning methods using lexical features. Useful for explaining why opinion classification differs from topic classification.

**Review note:** Foundational; abstract/metadata inspected.

<a id="r02"></a>
## R02: Thumbs Up or Thumbs Down? Semantic Orientation Applied to Unsupervised Classification of Reviews

- **Authors:** Peter Turney.
- **Source date:** 2002/7.
- **Source:** [R02 primary page](https://aclanthology.org/P02-1053/) · [PDF](https://aclanthology.org/P02-1053.pdf).

Early semantic-orientation method based on phrase associations with positive and negative reference terms. Useful historical contrast to supervised classifiers.

**Review note:** Foundational; abstract/metadata inspected.

<a id="r03"></a>
## R03: Baselines and Bigrams: Simple, Good Sentiment and Topic Classification

- **Authors:** Sida I. Wang; Christopher D. Manning.
- **Source date:** 2012/7.
- **Source:** [R03 primary page](https://aclanthology.org/P12-2018/) · [PDF](https://aclanthology.org/P12-2018.pdf).

Demonstrates the importance of word bigrams, Naive Bayes variants, and NB-SVM. The most useful paper here for defining a strong classical baseline.

**Review note:** Core reading; methods/results inspected; historical comparison.

<a id="r04"></a>
## R04: VADER: A Parsimonious Rule-Based Model for Sentiment Analysis of Social Media Text

- **Authors:** C. Hutto; Eric Gilbert.
- **Source date:** 2014/05/16.
- **Source:** [R04 primary page](https://ojs.aaai.org/index.php/ICWSM/article/view/14550) · [PDF](https://ojs.aaai.org/index.php/ICWSM/article/download/14550/14399).

VADER combines a sentiment lexicon with rules tailored to social-media language. Useful for explaining rule-based sentiment and score thresholds.

**Review note:** Core lexicon source; publisher page inspected.

<a id="r05"></a>
## R05: Loughran-McDonald Master Dictionary w/ Sentiment Word Lists

- **Authors:** Official resource; see source page.
- **Source date:** Ongoing resource.
- **Source:** [R05 primary page](https://sraf.nd.edu/loughranmcdonald-master-dictionary/).

Official financial dictionary resource, covering sentiment and other financial tone categories. Pair with the original journal paper R36.

**Review note:** Official resource rather than a separate research paper.

<a id="r06"></a>
## R06: Good Debt or Bad Debt: Detecting Semantic Orientations in Economic Texts

- **Authors:** Malo, Pekka; Sinha, Ankur; Takala, Pyry; Korhonen, Pekka; Wallenius, Jyrki.
- **Source date:** 2013/07/19.
- **Source:** [R06 primary page](https://arxiv.org/abs/1307.5336) · [PDF](https://arxiv.org/pdf/1307.5336).

Introduces the human-annotated financial phrase-bank and domain-aware semantic-orientation modeling. Relevant to label ambiguity and finance-specific evaluation.

**Review note:** 2013 preprint of work published in 2014; abstract/metadata inspected.

<a id="r07"></a>
## R07: SemEval-2014 Task 4: Aspect Based Sentiment Analysis

- **Authors:** Maria Pontiki; Dimitrios Galanis; John Pavlopoulos; Harris Papageorgiou; Ion Androutsopoulos; Suresh Manandhar.
- **Source date:** 2014/8.
- **Source:** [R07 primary page](https://aclanthology.org/S14-2004/) · [PDF](https://aclanthology.org/S14-2004.pdf).

Defines aspect-based sentiment tasks that distinguish extracting aspects from predicting polarity for a known aspect. Useful for explaining why document polarity is insufficient.

**Review note:** Benchmark/task paper; abstract/metadata inspected.

<a id="r08"></a>
## R08: Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank

- **Authors:** Richard Socher; Alex Perelygin; Jean Wu; Jason Chuang; Christopher D. Manning; Andrew Y. Ng; Christopher Potts.
- **Source date:** 2013/10.
- **Source:** [R08 primary page](https://aclanthology.org/D13-1170/) · [PDF](https://aclanthology.org/D13-1170.pdf).

Introduces the Stanford Sentiment Treebank and recursive compositional sentiment models. Useful background on phrase-level labels and composition.

**Review note:** Foundational neural method/dataset; abstract/metadata inspected.

<a id="r09"></a>
## R09: Convolutional Neural Networks for Sentence Classification

- **Authors:** Yoon Kim.
- **Source date:** 2014/10.
- **Source:** [R09 primary page](https://aclanthology.org/D14-1181/) · [PDF](https://aclanthology.org/D14-1181.pdf).

A CNN classifier using pretrained word embeddings. Useful example of learned local phrase features before the transformer era.

**Review note:** Neural method; abstract/metadata inspected.

<a id="r10"></a>
## R10: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

- **Authors:** Jacob Devlin; Ming-Wei Chang; Kenton Lee; Kristina Toutanova.
- **Source date:** 2019/6.
- **Source:** [R10 primary page](https://aclanthology.org/N19-1423/) · [PDF](https://aclanthology.org/N19-1423.pdf).

BERT contextual pretraining and fine-tuning. Useful technical foundation for the encoder-classifier family; it is not a sentiment-only model.

**Review note:** Transformer foundation; abstract/metadata inspected.

<a id="r11"></a>
## R11: DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter

- **Authors:** Sanh, Victor; Debut, Lysandre; Chaumond, Julien; Wolf, Thomas.
- **Source date:** 2019/10/02.
- **Source:** [R11 primary page](https://arxiv.org/abs/1910.01108) · [PDF](https://arxiv.org/pdf/1910.01108).

Knowledge distillation into a smaller BERT-family model. Useful for discussing compact contextual models and inference efficiency.

**Review note:** 2019 preprint; abstract/metadata inspected; no local timing reproduction.

<a id="r12"></a>
## R12: FinBERT: Financial Sentiment Analysis with Pre-trained Language Models

- **Authors:** Araci, Dogu.
- **Source date:** 2019/08/27.
- **Source:** [R12 primary page](https://arxiv.org/abs/1908.10063) · [PDF](https://arxiv.org/pdf/1908.10063).

Financial sentiment classification using BERT. Strong middle-category reference, with Financial PhraseBank and FiQA evaluation. Its baseline-tuning caveat matters when interpreting results.

**Review note:** Core reading; 2019 thesis/preprint; methods/results inspected.

<a id="r13"></a>
## R13: Sentiment Analysis in the Era of Large Language Models: A Reality Check

- **Authors:** Wenxuan Zhang; Yue Deng; Bing Liu; Sinno Pan; Lidong Bing.
- **Source date:** 2024/6.
- **Source:** [R13 primary page](https://aclanthology.org/2024.findings-naacl.246/) · [PDF](https://aclanthology.org/2024.findings-naacl.246.pdf).

Broad evaluation over 13 tasks and 26 datasets, including limited-label settings and structured sentiment extraction. The main comparative LLM reference, with explicit old-model and English-only limitations.

**Review note:** Core reading; cite NAACL Findings 2024 publication, not only its 2023 preprint; methods/results/limitations inspected.

<a id="r14"></a>
## R14: Is ChatGPT a Good Sentiment Analyzer? A Preliminary Study

- **Authors:** Wang, Zengzhi; Xie, Qiming; Feng, Yi; Ding, Zixiang; Yang, Zinong; Xia, Rui.
- **Source date:** 2023/04/10.
- **Source:** [R14 primary page](https://arxiv.org/abs/2304.04339) · [PDF](https://arxiv.org/pdf/2304.04339).

Evaluates ChatGPT on sentiment, opinions, and emotions, including standard, polarity-shift, and open-domain settings. Useful complementary evaluation dimensions.

**Review note:** 2023 preprint, revised 2024; abstract/metadata inspected; not a current-model benchmark.

<a id="r15"></a>
## R15: Efficient Few-Shot Learning Without Prompts

- **Authors:** Tunstall, Lewis; Reimers, Nils; Jo, Unso Eun Seo; Bates, Luke; Korat, Daniel; Wasserblat, Moshe; Pereg, Oren.
- **Source date:** 2022/09/22.
- **Source:** [R15 primary page](https://arxiv.org/abs/2209.11055) · [PDF](https://arxiv.org/pdf/2209.11055).

SetFit trains a sentence-transformer representation contrastively and fits a classification head with few labels. Useful counterexample to the claim that few-shot sentiment requires a large prompt-based model.

**Review note:** Core efficiency reference; 2022 preprint; abstract/metadata inspected.

<a id="r16"></a>
## R16: TweetEval: Unified Benchmark and Comparative Evaluation for Tweet Classification

- **Authors:** Francesco Barbieri; Jose Camacho-Collados; Luis Espinosa Anke; Leonardo Neves.
- **Source date:** 2020/11.
- **Source:** [R16 primary page](https://aclanthology.org/2020.findings-emnlp.148/) · [PDF](https://aclanthology.org/2020.findings-emnlp.148.pdf).

Unifies tweet classification tasks, including sentiment, under standardized datasets and evaluation. Useful for social-domain testing and task distinctions.

**Review note:** Benchmark paper; abstract/metadata inspected.

<a id="r17"></a>
## R17: GoEmotions: A Dataset of Fine-Grained Emotions

- **Authors:** Dorottya Demszky; Dana Movshovitz-Attias; Jeongwoo Ko; Alan Cowen; Gaurav Nemade; Sujith Ravi.
- **Source date:** 2020/7.
- **Source:** [R17 primary page](https://aclanthology.org/2020.acl-main.372/) · [PDF](https://aclanthology.org/2020.acl-main.372.pdf).

Fine-grained emotion dataset. Helps distinguish positive/negative sentiment from a richer emotion taxonomy.

**Review note:** Dataset paper; abstract/metadata inspected.

<a id="r18"></a>
## R18: Beyond Accuracy: Behavioral Testing of NLP Models with CheckList

- **Authors:** Marco Tulio Ribeiro; Tongshuang Wu; Carlos Guestrin; Sameer Singh.
- **Source date:** 2020/7.
- **Source:** [R18 primary page](https://aclanthology.org/2020.acl-main.442/) · [PDF](https://aclanthology.org/2020.acl-main.442.pdf).

Capability-oriented behavioral tests for NLP models. Useful foundation for negation, invariance, and other diagnostic slices beyond aggregate accuracy.

**Review note:** Core evaluation reference; abstract/metadata inspected.

<a id="r19"></a>
## R19: On Calibration of Modern Neural Networks

- **Authors:** Guo, Chuan; Pleiss, Geoff; Sun, Yu; Weinberger, Kilian Q..
- **Source date:** 2017/06/14.
- **Source:** [R19 primary page](https://arxiv.org/abs/1706.04599) · [PDF](https://arxiv.org/pdf/1706.04599).

Studies calibration of neural-network confidence and temperature scaling. Useful when probabilities control human review or model escalation.

**Review note:** General calibration paper; abstract/metadata inspected; calibration under shift still needs testing.

<a id="r20"></a>
## R20: Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting

- **Authors:** Sclar, Melanie; Choi, Yejin; Tsvetkov, Yulia; Suhr, Alane.
- **Source date:** 2023/10/17.
- **Source:** [R20 primary page](https://arxiv.org/abs/2310.11324) · [PDF](https://arxiv.org/pdf/2310.11324).

Studies sensitivity to meaning-preserving prompt formatting. Useful for explaining why prompt choice is an experimental variable and why a single template can mislead.

**Review note:** 2023 preprint / ICLR 2024; abstract/metadata inspected; largest reported effects are not universal sentiment effects.

<a id="r21"></a>
## R21: BloombergGPT: A Large Language Model for Finance

- **Authors:** Wu, Shijie; Irsoy, Ozan; Lu, Steven; Dabravolski, Vadim; Dredze, Mark; Gehrmann, Sebastian; Kambadur, Prabhanjan; Rosenberg, David; Mann, Gideon.
- **Source date:** 2023/03/30.
- **Source:** [R21 primary page](https://arxiv.org/abs/2303.17564) · [PDF](https://arxiv.org/pdf/2303.17564).

A large domain-oriented language model trained for financial tasks. Useful for explaining financial domain pretraining and broad evaluation.

**Review note:** 2023 preprint; abstract/metadata inspected; not evidence of a currently available best sentiment system.

<a id="r22"></a>
## R22: FinGPT: Open-Source Financial Large Language Models

- **Authors:** Yang, Hongyang; Liu, Xiao-Yang; Wang, Christina Dan.
- **Source date:** 2023/06/09.
- **Source:** [R22 primary page](https://arxiv.org/abs/2306.06031) · [PDF](https://arxiv.org/pdf/2306.06031).

Open-source financial LLM framework and adaptation direction. Useful background for instruction-tuned financial models and financial data pipelines.

**Review note:** 2023 preprint; abstract/metadata inspected; implementation is R33.

<a id="r23"></a>
## R23: SemEval-2017 Task 5: Fine-Grained Sentiment Analysis on Financial Microblogs and News

- **Authors:** Keith Cortis; André Freitas; Tobias Daudert; Manuela Huerlimann; Manel Zarrouk; Siegfried Handschuh; Brian Davis.
- **Source date:** 2017/8.
- **Source:** [R23 primary page](https://aclanthology.org/S17-2089/) · [PDF](https://aclanthology.org/S17-2089.pdf).

Fine-grained financial sentiment task using microblogs and news. Useful for target-linked sentiment, continuous scores, and official financial task metrics.

**Review note:** Benchmark/task paper; abstract/metadata inspected.

<a id="r24"></a>
## R24: Large Language Model Adaptation for Financial Sentiment Analysis

- **Authors:** Inserte, Pau Rodriguez; Nakhlé, Mariam; Qader, Raheel; Caillaut, Gaetan; Liu, Jingshu.
- **Source date:** 2024/01/26.
- **Source:** [R24 primary page](https://arxiv.org/abs/2401.14777) · [PDF](https://arxiv.org/pdf/2401.14777).

Investigates financial adaptation of foundation models below 1.5B parameters using financial text, instructions, and augmentation. Shows why domain adaptation and model size should be separate variables.

**Review note:** 2024 preprint; methods/results/limitations inspected; findings depend on its training and evaluation setup.

<a id="r25"></a>
## R25: BESSTIE: A Benchmark for Sentiment and Sarcasm Classification for Varieties of English

- **Authors:** Dipankar Srirag; Aditya Joshi; Jordan Painter; Diptesh Kanojia.
- **Source date:** 2025/7.
- **Source:** [R25 primary page](https://aclanthology.org/2025.findings-acl.441/) · [PDF](https://aclanthology.org/2025.findings-acl.441.pdf).

BESSTIE evaluates sentiment and sarcasm across Australian, Indian, and British English. Useful contemporary evidence on cross-variety generalization and annotation limitations.

**Review note:** Core recent reading; ACL Findings 2025; methods/results/limitations inspected; sentiment task is binary.

<a id="r26"></a>
## R26: Comparing LLMs for Sentiment Analysis in Financial Market News

- **Authors:** Teles, Lucas Eduardo Pereira; Figueiredo, Carlos M. S..
- **Source date:** 2025/10/03.
- **Source:** [R26 primary page](https://arxiv.org/abs/2510.15929) · [PDF](https://arxiv.org/pdf/2510.15929).

Financial comparison across several datasets, with both generative and encoder models. Useful as a critical-reading case: mixed taxonomy, omitted strong linear baselines, and a label-description inconsistency.

**Review note:** 2025 preprint; methods/results inspected; use cautiously, as discussed in the research.

<a id="r27"></a>
## R27: Uncovering Sentiment Analysis Circuit in Large Language Model

- **Authors:** Shichen Li; Zhouyang Wang; Zhongqing Wang (王中卿); Peifeng Li (李培峰).
- **Source date:** 2026/7.
- **Source:** [R27 primary page](https://aclanthology.org/2026.acl-long.928/) · [PDF](https://aclanthology.org/2026.acl-long.928.pdf).

Uses sparse autoencoders and circuit interventions to study why sentiment information can be represented internally yet elicited inconsistently by different prompts. Useful current evidence on robustness and mechanistic interpretability.

**Review note:** Core recent reading; ACL 2026; methods/results/limitations inspected; specific open-weight models and binary-filtered tasks.

<a id="r35"></a>
## R35: Beyond Benchmark Accuracy: Robustness Evaluation of Hinglish Sentiment Models

- **Authors:** Chennuru Rahul; Kolawole Adebayo.
- **Source date:** 2026/7.
- **Source:** [R35 primary page](https://aclanthology.org/2026.dravidianlangtech-1.2/) · [PDF](https://aclanthology.org/2026.dravidianlangtech-1.2.pdf).

Diagnostic Hinglish sentiment study comparing in-distribution, adversarial, and cross-domain results. Supports stress testing but contains a chance-baseline description error and limited evaluation scope.

**Review note:** 2026 workshop paper; methods/results/limitations inspected; supplementary evidence, not a decisive ranking.

<a id="r36"></a>
## R36: When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10‐Ks

- **Authors:** TIM LOUGHRAN; BILL MCDONALD.
- **Source date:** [2011, 1, 6].
- **Source:** [R36 primary page](https://doi.org/10.1111/j.1540-6261.2010.01625.x).

Original financial dictionary paper showing the mismatch between general negative word lists and financial language. Important domain-validity motivation.

**Review note:** Journal of Finance, 2011; publisher-supplied abstract/metadata via Crossref inspected; full paper not reviewed.

<a id="r37"></a>
## R37: Giving Content to Investor Sentiment: The Role of Media in the Stock Market

- **Authors:** PAUL C. TETLOCK.
- **Source date:** [2007, 5, 8].
- **Source:** [R37 primary page](https://doi.org/10.1111/j.1540-6261.2007.01232.x).

Historical study of media pessimism and market prices/volume. Motivates financial text measurement while leaving modern causal and trading claims to separate evaluation.

**Review note:** Journal of Finance, 2007; publisher-supplied abstract/metadata via Crossref inspected; full paper not reviewed.

<a id="r38"></a>
## R38: SentiWordNet 3.0: An Enhanced Lexical Resource for Sentiment Analysis and Opinion Mining

- **Authors:** Stefano Baccianella; Andrea Esuli; Fabrizio Sebastiani.
- **Source date:** 2010/5.
- **Source:** [R38 primary page](https://aclanthology.org/L10-1531/) · [PDF](https://aclanthology.org/L10-1531.pdf).

Word-sense-aware lexicon assigning sentiment/objectivity scores to WordNet synsets. Extends the lexicon taxonomy beyond surface word lookup.

**Review note:** LREC 2010; primary abstract/metadata inspected; no local word-sense implementation run.

<a id="r39"></a>
## R39: TinyBERT: Distilling BERT for Natural Language Understanding

- **Authors:** Xiaoqi Jiao; Yichun Yin; Lifeng Shang; Xin Jiang; Xiao Chen; Linlin Li; Fang Wang; Qun Liu.
- **Source date:** 2020/11.
- **Source:** [R39 primary page](https://aclanthology.org/2020.findings-emnlp.372/) · [PDF](https://aclanthology.org/2020.findings-emnlp.372.pdf).

Transformer distillation at pretraining and task stages. Its four-layer student reports over 96.8% of BERT-Base GLUE performance, 7.5-times smaller size and 9.4-times faster inference in the original setup.

**Review note:** EMNLP Findings 2020; abstract/metadata inspected; historical GLUE and efficiency figures are not universal sentiment accuracy or current timings.

<a id="r40"></a>
## R40: Benchmarking large language models for target-based financial sentiment and stock return

- **Authors:** Muhammad, Iftikhar; Rospocher, Marco; Knez, Timotej; Žitnik, Slavko.
- **Source date:** 2026/07/02.
- **Source:** [R40 primary page](https://link.springer.com/article/10.1007/s41060-026-01201-x) · [PDF](https://link.springer.com/content/pdf/10.1007/s41060-026-01201-x.pdf).

Target-aware Bloomberg financial sentiment benchmark reporting five-shot DeepSeek-R1 macro F1 of 0.87, on 1,334 target cases from 1,162 articles. Adds complementary LLM evidence with dataset, serving, and reporting limitations.

**Review note:** Published online 2 July 2026, with a December issue date and an earlier 2025 conference version. Full publisher HTML methods/results inspected; Table 3 has an accuracy/weighted-recall inconsistency for one baseline configuration; no local reproduction.

<a id="r41"></a>
## R41: Artificial Intelligence Risk Management Framework (AI RMF 1.0)

- **Authors:** Elham Tabassi.
- **Source date:** 2023/01/26.
- **Source:** [R41 primary page](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/).

Official framework describing contextual trustworthiness tradeoffs, including validity, reliability, transparency, interpretability, privacy, and fairness.

**Review note:** NIST AI RMF 1.0, January 2023; official section 3 and publication page inspected. Voluntary framework, not a sentiment benchmark or model-family prescription.

<a id="r42"></a>
## R42: Aspect-Based Sentiment Analysis for Open-Ended HR Survey Responses

- **Authors:** Lois Rink; Job Meijdam; David Graus.
- **Source date:** 2024/3.
- **Source:** [R42 primary page](https://aclanthology.org/2024.nlp4hr-1.2/) · [PDF](https://aclanthology.org/2024.nlp4hr-1.2.pdf).

Aspect-based sentiment application using 1,458 Dutch HR survey responses and Dutch BERT-based few-shot approaches. Adds an industrial survey application with multiple feedback aspects.

**Review note:** NLP4HR 2024; abstract/metadata inspected. Independently identified; not assumed to match the missing survey citation in the user draft.

<a id="r28"></a>
<a id="r29"></a>
<a id="r30"></a>
<a id="r31"></a>
<a id="r32"></a>
<a id="r33"></a>
<a id="r34"></a>
## Implementations, checkpoints, and datasets

These upstream projects provide methods, checkpoints, and datasets. The local
[code](code/README.md) uses scikit-learn and vaderSentiment; full upstream
repositories have not been vendored or reproduced.
License metadata is not a substitute for reviewing the terms of any separate
model weights, corpus, or downloaded asset.

| Resource | Useful starting point | Why include it | Practical caution |
|---|---|---|---|
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) / [text feature documentation](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) [R28](#r28) | `TfidfVectorizer`, `Pipeline`, `LogisticRegression`, `LinearSVC` | Strong sparse baselines; training-only fitting through a pipeline | Preserve negation; tune n-grams and regularization on development data |
| [vaderSentiment](https://github.com/cjhutto/vaderSentiment) [R29](#r29) | `SentimentIntensityAnalyzer` | Reproducible lexicon/rule baseline | Compound scores are not calibrated class probabilities; financial applicability needs testing |
| [ProsusAI/finbert](https://github.com/ProsusAI/finbert) [R30] | Original financial classifier implementation | Connects the FinBERT research to training/inference code | Original dependency versions may need an isolated environment; repository code and published checkpoint are different artifacts |
| [ProsusAI/finbert model card](https://huggingface.co/ProsusAI/finbert) [R34] | Hugging Face text-classification checkpoint | Practical pretrained financial sentiment baseline | Pin revision and tokenizer; inspect `id2label`; check benchmark fine-tuning overlap |
| [DAMO-NLP-SG/LLM-Sentiment](https://github.com/DAMO-NLP-SG/LLM-Sentiment) [R31] | Task definitions, zero/few-shot scripts, prompts, evaluation | Implementation accompanying R13 / SentiEval | Old API models and SDK assumptions may no longer reproduce the original setup |
| [huggingface/setfit](https://github.com/huggingface/setfit) [R32] | Sentence-transformer adaptation plus classifier | Efficient limited-label competitor | Use identical support sets and report training seeds; pretrained embedding choice matters |
| [AI4Finance-Foundation/FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) [R33] | Financial data/model adaptation workflows | Examples of task-adapted generative financial NLP | Record the exact subproject/checkpoint; project-wide claims do not validate every released model |
| [Loughran–McDonald dictionary](https://sraf.nd.edu/loughranmcdonald-master-dictionary/) [R05] | Domain word lists | Financial tone baseline and domain vocabulary reference | Record dictionary vintage, count normalization, and applicable use terms |
| [BESSTIE dataset](https://huggingface.co/datasets/unswnlporg/BESSTIE) [R25] | English-variety sentiment and sarcasm data | Cross-variety evaluation beyond generic English benchmarks | Sentiment is binary; verify the current dataset card and license before download |

The BESSTIE dataset link is provided by the verified paper; its dataset contents
were not downloaded or independently audited here.

For an experiment, use an isolated environment and pin dependencies and model
revisions. Start with the strong TF-IDF baseline and one contextual classifier,
then add a prompted LLM under the same labels and input context. The
[evaluation protocol](EXPERIMENTS.md) describes how to avoid misleading
comparisons.

## Review scope

This is a targeted literature review. Methods/results/limitations were inspected
in eight PDFs (R03, R12, R13, R24, R25, R26, R27, R35), the publisher HTML for
R40, and the official framework section for R41. Other entries were reviewed
through abstracts, bibliographic metadata, documentation, or model/repository
cards. R36 and R37 were checked through publisher-supplied metadata rather than
the full journal articles. Published experiments have not been reproduced here.

The contributed draft included numbered citations without a bibliography. Its
unidentified survey, Nigerian-tweet, review, and edge-AI studies were not used
as verified empirical evidence. Independently identified sources support the
findings included in [Research](RESEARCH.md).
