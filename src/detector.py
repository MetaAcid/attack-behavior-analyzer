def calculate_risk_level(requests, failed_logins, unique_paths, score):
    if score < -0.10 or requests >= 250 or failed_logins >= 40 or unique_paths >= 60:
        return "HIGH"
    if score < 0 or requests >= 100 or failed_logins >= 10 or unique_paths >= 20:
        return "MEDIUM"
    return "LOW"


def explain_anomaly(requests, failed_logins, unique_paths, time_between_requests, score):
    reasons = []

    if requests >= 100:
        reasons.append("high request volume")

    if failed_logins >= 10:
        reasons.append("multiple failed login attempts")

    if unique_paths >= 20:
        reasons.append("unusually broad path access")

    if time_between_requests <= 0.5:
        reasons.append("very short interval between requests")

    if score < 0:
        reasons.append("low anomaly score from model")

    if not reasons:
        return "Suspicious behavior detected based on anomaly model output"

    return "Suspicious behavior detected: " + ", ".join(reasons)


def detect_anomalies(df, predictions, scores):
    results = []

    for i, pred in enumerate(predictions):
        row = df.iloc[i]

        label = "ANOMALY" if pred == -1 else "NORMAL"
        score = float(scores[i])

        if pred == -1:
            requests = int(row["requests"])
            failed_logins = int(row["failed_logins"])
            unique_paths = int(row["unique_paths"])
            time_between_requests = float(row["time_between_requests"])

            results.append({
                "ip": str(row["IP"]),
                "requests": requests,
                "failed_logins": failed_logins,
                "unique_paths": unique_paths,
                "time_between_requests": time_between_requests,
                "anomaly_score": round(score, 4),
                "label": label,
                "risk_level": calculate_risk_level(
                    requests,
                    failed_logins,
                    unique_paths,
                    score
                ),
                "description": explain_anomaly(
                    requests,
                    failed_logins,
                    unique_paths,
                    time_between_requests,
                    score
                )
            })

    return results