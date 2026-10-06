"""Strict input validation and elementary split-leakage checks."""

import csv
import hashlib
from dataclasses import dataclass
from pathlib import Path

LABELS = ("negative", "neutral", "positive")


@dataclass(frozen=True)
class Example:
    id: str
    text: str
    label: str
    group_id: str = ""


def canonical_text(text):
    return " ".join(text.casefold().split())


def read_examples(path):
    examples = []
    ids, texts = set(), set()
    with Path(path).open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not {"id", "text", "label"}.issubset(reader.fieldnames or []):
            raise ValueError("CSV requires id,text,label columns (optional: group_id)")
        for row_number, row in enumerate(reader, 2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"Malformed CSV row {row_number}")
            item = Example(row["id"].strip(), row["text"].strip(),
                           row["label"].strip(), row.get("group_id", "").strip())
            if not item.id or not item.text or item.label not in LABELS:
                raise ValueError(f"Invalid id, text, or label at row {row_number}")
            key = canonical_text(item.text)
            if item.id in ids or key in texts:
                raise ValueError(f"Duplicate id or normalized text at row {row_number}")
            ids.add(item.id)
            texts.add(key)
            examples.append(item)
    if not examples:
        raise ValueError("Dataset is empty")
    return examples


def check_splits(train, test):
    for name, key in (("id", lambda x: x.id),
                      ("normalized text", lambda x: canonical_text(x.text)),
                      ("group_id", lambda x: x.group_id)):
        train_values = {key(item) for item in train if key(item)}
        test_values = {key(item) for item in test if key(item)}
        if train_values & test_values:
            raise ValueError(f"Train/test overlap in {name}")
    if {item.label for item in train} != set(LABELS):
        raise ValueError("Training data must contain all three configured classes")


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_predictions(path, examples):
    """Require exactly one valid prediction for each test id, regardless of order."""
    predictions = {}
    with Path(path).open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not {"id", "prediction"}.issubset(reader.fieldnames or []):
            raise ValueError("Prediction CSV requires id,prediction columns")
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError("Malformed prediction CSV row")
            item_id, label = row["id"].strip(), row["prediction"].strip()
            if item_id in predictions or label not in LABELS:
                raise ValueError("Duplicate prediction id or invalid prediction label")
            predictions[item_id] = label
    if set(predictions) != {item.id for item in examples}:
        raise ValueError("Prediction ids must match test ids exactly")
    return [predictions[item.id] for item in examples]
