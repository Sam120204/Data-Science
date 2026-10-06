"""Shared fixed-label metrics and transparent run artifacts."""

import csv
import importlib.metadata
import json
import platform
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score

from .data import LABELS, file_hash


def metrics(examples, predictions):
    if len(examples) != len(predictions) or any(label not in LABELS for label in predictions):
        raise ValueError("Predictions must supply one allowed label for every example")
    truth = [item.label for item in examples]
    return {
        "accuracy": float(accuracy_score(truth, predictions)),
        "macro_f1": float(f1_score(truth, predictions, labels=LABELS,
                                   average="macro", zero_division=0)),
        "per_class": classification_report(truth, predictions, labels=LABELS,
                                            output_dict=True, zero_division=0),
        "confusion_matrix": confusion_matrix(truth, predictions, labels=LABELS).tolist(),
        "label_order": list(LABELS),
        "absent_class_policy": "All three labels included; undefined precision/recall/F1 = 0",
    }


def dataset_record(path, examples):
    return {"file": Path(path).name, "sha256": file_hash(path),
            "rows": len(examples), "class_counts": dict(Counter(item.label for item in examples))}


def write_run(args, test, predictions, train=None, timing=None):
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=False)
    packages = {}
    for name in ("numpy", "scikit-learn", "vaderSentiment", "torch", "transformers"):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            pass
    result = {
        "schema_version": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "purpose": args.purpose,
        "dataset_note": args.dataset_note,
        "model": args.model,
        "settings": {"seed": args.seed, "features": args.features,
                     "revision": args.revision, "batch_size": args.batch_size},
        "environment": {"python": platform.python_version(), "platform": platform.platform(),
                        "packages": packages},
        "test": dataset_record(args.test, test),
        "train": dataset_record(args.train, train) if train is not None else None,
        "prediction_source_sha256": file_hash(args.predictions) if args.predictions else None,
        "timing_seconds": timing,
        "timing_scope": "One local wall-clock run; initialization, fit, and full-test prediction. Not p95 latency or a cost benchmark.",
        "metrics": metrics(test, predictions),
    }
    with (output / "predictions.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["id", "label", "prediction", "correct"])
        for item, prediction in zip(test, predictions):
            writer.writerow([item.id, item.label, prediction, item.label == prediction])
    (output / "metrics.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result
