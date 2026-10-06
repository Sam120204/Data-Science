"""Behavioral checks for split isolation, scoring, and artifact integrity."""

import csv
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from data import Example, check_splits, read_examples, read_predictions
from evaluate import metrics, write_run
from models import FinBert, sparse_pipeline


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.directory = Path(self.temporary.name)
        self.addCleanup(self.temporary.cleanup)
        self.train = [Example("a", "great quality", "positive", "g1"),
                      Example("b", "terrible quality", "negative", "g2"),
                      Example("c", "quality report", "neutral", "g3")]
        self.test = [Example("d", "unseentesttoken quality", "neutral", "g4")]

    def csv(self, name, headers, rows):
        path = self.directory / name
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(headers)
            writer.writerows(rows)
        return path

    def test_overlap_id_rejected(self):
        with self.assertRaisesRegex(ValueError, "overlap in id"):
            check_splits(self.train, [Example("a", "a distinct test", "positive")])

    def test_overlap_normalized_text_rejected(self):
        with self.assertRaisesRegex(ValueError, "normalized text"):
            check_splits(self.train, [Example("z", " GREAT   Quality ", "positive")])

    def test_overlap_group_rejected(self):
        with self.assertRaisesRegex(ValueError, "group_id"):
            check_splits(self.train, [Example("z", "different article text", "positive", "g1")])

    def test_missing_training_class_rejected(self):
        with self.assertRaisesRegex(ValueError, "all three"):
            check_splits(self.train[:2], self.test)

    def test_duplicate_text_rejected(self):
        path = self.csv("duplicate.csv", ["id", "text", "label"],
                        [["a", "Good item", "positive"], ["b", "good  ITEM", "positive"]])
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            read_examples(path)

    def test_bad_inputs_rejected(self):
        cases = [(["text", "label"], [["item", "positive"]]),
                 (["id", "text", "label"], [["a", "", "positive"]]),
                 (["id", "text", "label"], [["a", "item", "mixed"]]),
                 (["id", "text", "label"], [["a", "item"]]),
                 (["id", "text", "label"], [])]
        for index, (headers, rows) in enumerate(cases):
            with self.subTest(index=index), self.assertRaises(ValueError):
                read_examples(self.csv(f"invalid{index}.csv", headers, rows))

    def test_test_vocabulary_is_not_fitted(self):
        for classifier in ("logreg", "linearsvc"):
            with self.subTest(classifier=classifier):
                pipeline = sparse_pipeline(classifier, "word", 42)
                pipeline.fit([x.text for x in self.train], [x.label for x in self.train])
                pipeline.predict([x.text for x in self.test])
                self.assertNotIn("unseentesttoken", pipeline.named_steps["tfidf"].vocabulary_)
                self.assertIn("great", pipeline.named_steps["tfidf"].vocabulary_)

    def test_metric_order_and_missing_class_policy(self):
        result = metrics(self.train, ["positive", "negative", "negative"])
        self.assertAlmostEqual(result["accuracy"], 2 / 3)
        self.assertAlmostEqual(result["macro_f1"], 5 / 9)
        self.assertEqual(result["confusion_matrix"], [[1, 0, 0], [1, 0, 0], [0, 0, 1]])
        absent = metrics(self.test, ["neutral"])
        self.assertAlmostEqual(absent["macro_f1"], 1 / 3)

    def test_imported_predictions_align_by_id(self):
        path = self.csv("predictions.csv", ["id", "prediction"],
                        [["c", "neutral"], ["a", "positive"], ["b", "negative"]])
        self.assertEqual(read_predictions(path, self.train), ["positive", "negative", "neutral"])

    def test_imported_predictions_cannot_drop_or_duplicate_items(self):
        for index, rows in enumerate([[["d", "unknown"]], [],
                                      [["d", "neutral"], ["d", "positive"]],
                                      [["extra", "neutral"]]]):
            with self.subTest(index=index), self.assertRaises(ValueError):
                read_predictions(self.csv(f"pred{index}.csv", ["id", "prediction"], rows), self.test)

    def test_artifacts_preserve_purpose_and_prevent_overwrite(self):
        test_file = self.csv("test.csv", ["id", "text", "label"], [["d", "some report", "neutral"]])
        args = SimpleNamespace(output=self.directory / "run", purpose="smoke", dataset_note="constructed",
                               model="imported", seed=42, features="word", revision="example-v1",
                               batch_size=16, test=test_file, train=None, predictions=None)
        write_run(args, self.test, ["neutral"])
        result = json.loads((args.output / "metrics.json").read_text())
        self.assertEqual(result["purpose"], "smoke")
        self.assertEqual(len(result["test"]["sha256"]), 64)
        self.assertTrue((args.output / "predictions.csv").is_file())
        with self.assertRaises(FileExistsError):
            write_run(args, self.test, ["neutral"])

    def test_finbert_refuses_unpinned_revision_before_loading(self):
        for revision in (None, "main", "a1b2"):
            with self.subTest(revision=revision), self.assertRaisesRegex(ValueError, "commit SHA"):
                FinBert(revision, 16)


if __name__ == "__main__":
    unittest.main()
