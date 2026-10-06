# Implementations, checkpoints, and datasets

These upstream projects were inspected as research resources. They were not
cloned, installed, or benchmarked. Checked repository commits and
GitHub-reported licenses are in
[Repository revisions](../sources/repository-snapshots.json).
License metadata is not a substitute for reviewing the terms of any separate
model weights, corpus, or downloaded asset.

| Resource | Useful starting point | Why include it | Practical caution |
|---|---|---|---|
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) / [text feature documentation](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) [R28] | `TfidfVectorizer`, `Pipeline`, `LogisticRegression`, `LinearSVC` | Strong sparse baselines; training-only fitting through a pipeline | Preserve negation; tune n-grams and regularization on development data |
| [vaderSentiment](https://github.com/cjhutto/vaderSentiment) [R29] | `SentimentIntensityAnalyzer` | Reproducible lexicon/rule baseline | Compound scores are not calibrated class probabilities; financial applicability needs testing |
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
[evaluation protocol](../methodology/evaluation-protocol.md) describes how to avoid misleading
comparisons.
