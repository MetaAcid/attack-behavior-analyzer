def detect_anomalies(df, predictions):
    results = []

    for i, pred in enumerate(predictions):
        if pred == -1:
            row = df.iloc[i]

            results.append({
                "ip": str(row["IP"]),
                "requests": int(row["requests"]),
                "failed_logins": int(row["failed_logins"]),
                "unique_paths": int(row["unique_paths"]),
                "time_between_requests": float(row["time_between_requests"]),
                "description": "Potentially anomalous behavior based on traffic volume, failed logins, and request patterns"
            })

    return results