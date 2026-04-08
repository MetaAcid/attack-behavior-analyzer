def prepare_features(df):
    required_columns = [
        "requests",
        "failed_logins",
        "unique_paths",
        "time_between_requests"
    ]

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    return df[required_columns]