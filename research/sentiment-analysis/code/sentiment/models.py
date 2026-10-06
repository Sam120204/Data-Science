"""Small baseline implementations; no upstream repository code is vendored."""

from collections import Counter

from .data import LABELS


def sparse_pipeline(model, features, seed):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import Pipeline
    from sklearn.svm import LinearSVC

    vectorizer = TfidfVectorizer(
        analyzer="word" if features == "word" else "char_wb",
        ngram_range=(1, 2) if features == "word" else (3, 5),
        lowercase=True, sublinear_tf=True, stop_words=None,
    )
    classifier = (LogisticRegression(C=1.0, max_iter=2000, random_state=seed)
                  if model == "logreg" else
                  LinearSVC(C=1.0, dual=True, random_state=seed))
    return Pipeline([("tfidf", vectorizer), ("classifier", classifier)])


class Majority:
    def fit(self, texts, labels):
        counts = Counter(labels)
        self.label = max(LABELS, key=lambda label: counts[label])
        return self

    def predict(self, texts):
        return [self.label] * len(texts)


class Vader:
    def __init__(self):
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
        self.analyzer = SentimentIntensityAnalyzer()

    def predict(self, texts):
        predictions = []
        for text in texts:
            score = self.analyzer.polarity_scores(text)["compound"]
            predictions.append("positive" if score >= 0.05 else
                               "negative" if score <= -0.05 else "neutral")
        return predictions


class FinBert:
    """Inference only. Caller supplies an immutable Hugging Face commit revision."""

    def __init__(self, revision, batch_size):
        import re
        if not revision or not re.fullmatch(r"[0-9a-f]{40}", revision):
            raise ValueError("FinBERT requires a 40-character model commit SHA")
        from transformers import AutoModelForSequenceClassification, AutoTokenizer
        import torch
        self.torch = torch
        self.batch_size = batch_size
        self.tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert", revision=revision)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "ProsusAI/finbert", revision=revision).eval()
        self.labels = {int(k): str(v).lower() for k, v in self.model.config.id2label.items()}
        if set(self.labels.values()) != set(LABELS):
            raise ValueError("Checkpoint label mapping differs from the configured labels")

    def predict(self, texts):
        predictions = []
        for start in range(0, len(texts), self.batch_size):
            tokens = self.tokenizer(texts[start:start + self.batch_size],
                                    padding=True, truncation=True, max_length=512,
                                    return_tensors="pt")
            with self.torch.inference_mode():
                indices = self.model(**tokens).logits.argmax(dim=-1).tolist()
            predictions.extend(self.labels[index] for index in indices)
        return predictions
