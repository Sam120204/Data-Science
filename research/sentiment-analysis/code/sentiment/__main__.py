import argparse
from pathlib import Path
from time import perf_counter

from .data import check_splits, read_examples, read_predictions
from .evaluate import write_run
from .models import FinBert, Majority, Vader, sparse_pipeline


def main():
    parser = argparse.ArgumentParser(description="Run or score three-class sentiment baselines")
    parser.add_argument("--model", required=True,
                        choices=["majority", "logreg", "linearsvc", "vader", "finbert", "imported"])
    parser.add_argument("--train", type=Path)
    parser.add_argument("--test", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--purpose", required=True, choices=["smoke", "benchmark"])
    parser.add_argument("--dataset-note", required=True, help="Origin, labeling rubric, and split description")
    parser.add_argument("--features", choices=["word", "char"], default="word")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--revision", help="Immutable FinBERT commit SHA, or external model identifier")
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--predictions", type=Path, help="For imported mode: id,prediction CSV")
    args = parser.parse_args()
    try:
        if args.output.exists():
            raise ValueError("Output already exists; choose a new directory to preserve runs")
        if args.batch_size <= 0 or not args.dataset_note.strip():
            raise ValueError("Batch size and dataset note must be nonempty/positive")
        test = read_examples(args.test)
        train = read_examples(args.train) if args.train else None
        if train is not None:
            check_splits(train, test)
        supervised = args.model in {"majority", "logreg", "linearsvc"}
        if supervised and train is None:
            raise ValueError("This model requires --train")
        if args.predictions and args.model != "imported":
            raise ValueError("--predictions is only valid for imported mode")
        if args.model == "imported":
            if not args.predictions or not args.revision:
                raise ValueError("Imported predictions require --predictions and --revision")
            predictions = read_predictions(args.predictions, test)
            timing = None
        else:
            start = perf_counter()
            model = (sparse_pipeline(args.model, args.features, args.seed) if args.model in {"logreg", "linearsvc"}
                     else Majority() if args.model == "majority"
                     else Vader() if args.model == "vader"
                     else FinBert(args.revision, args.batch_size))
            initialized = perf_counter()
            if supervised:
                model.fit([item.text for item in train], [item.label for item in train])
            fitted = perf_counter()
            predictions = list(model.predict([item.text for item in test]))
            timing = {"initialization": initialized - start, "fit": fitted - initialized,
                      "full_test_prediction": perf_counter() - fitted}
        result = write_run(args, test, predictions, train, timing)
        print(f"{args.model}: {args.purpose}; {len(test)} items; macro F1 {result['metrics']['macro_f1']:.4f}")
        print(f"Saved metrics and predictions to {args.output}")
    except (ValueError, OSError, ImportError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
