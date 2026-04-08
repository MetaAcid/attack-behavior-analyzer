import argparse
from pathlib import Path

from data_loader import load_data
from feature_engineering import prepare_features
from model import train_model, predict
from detector import detect_anomalies
from reporter import save_results, print_results


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
        default="output/anomalies.json"
    )

    args = parser.parse_args()

    df = load_data(args.data)
    features = prepare_features(df)

    model = train_model(features)
    predictions = predict(model, features)

    results = detect_anomalies(df, predictions)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print_results(results)
    save_results(results, str(output_path))


if __name__ == "__main__":
    main()