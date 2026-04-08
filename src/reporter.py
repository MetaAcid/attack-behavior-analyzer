import json


def build_summary(results):
    summary = {
        "total_anomalies": len(results),
        "high": 0,
        "medium": 0,
        "low": 0
    }

    for result in results:
        level = result.get("risk_level", "").lower()
        if level in summary:
            summary[level] += 1

    return summary


def save_results(report, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)


def print_results(results):
    print("\n=== ANOMALIES DETECTED ===")
    print("=" * 30)

    if not results:
        print("No anomalies found.")
        return

    for r in results:
        print(f"\nIP: {r['ip']}")
        print(f"Requests: {r['requests']}")
        print(f"Failed logins: {r['failed_logins']}")
        print(f"Unique paths: {r['unique_paths']}")
        print(f"Time between requests: {r['time_between_requests']}")
        print(f"Risk level: {r['risk_level']}")
        print(f"Description: {r['description']}")