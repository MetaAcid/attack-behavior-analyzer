import argparse
from pathlib import Path
import sys

from data_loader import load_data
from feature_engineering import prepare_features
from model import train_model, predict, anomaly_scores
from detector import detect_anomalies
from reporter import save_results, print_results, build_summary, save_enriched_csv


def main():
    parser = argparse.ArgumentParser(
        description="Attack Behavior Analyzer"
    )
    parser.add_argument(
        "--data",
        default="data/sample_logs.csv",
        help="Path to dataset"
    )
    parser.add_argument(
        "--output",
        default="output/anomalies.json",
        help="Path to output JSON report"
    )
    parser.add_argument(
        "--csv-output",
        default="output/enriched_results.csv",
        help="Path to enriched CSV output"
    )

    args = parser.parse_args()

    try:
        df = load_data(args.data)
        features = prepare_features(df)

        model = train_model(features)
        predictions = predict(model, features)
        scores = anomaly_scores(model, features)

        df["prediction"] = ["ANOMALY" if p == -1 else "NORMAL" for p in predictions]
        df["anomaly_score"] = [round(float(s), 4) for s in scores]

        results = detect_anomalies(df, predictions, scores)
        summary = build_summary(results)

        report = {
            "dataset": args.data,
            "summary": summary,
            "anomalies": results
        }

        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        csv_output_path = Path(args.csv_output)
        csv_output_path.parent.mkdir(parents=True, exist_ok=True)

        print_results(results)
        save_results(report, str(output_path))
        save_enriched_csv(df, str(csv_output_path))

        print(f"\nJSON report saved to: {output_path}")
        print(f"CSV report saved to: {csv_output_path}")
        return 0

    except FileNotFoundError as error:
        print(f"\n[ERROR] File not found: {error}")
        return 1

    except ValueError as error:
        print(f"\n[ERROR] Invalid data: {error}")
        return 1

    except Exception as error:
        print(f"\n[ERROR] Unexpected failure: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())