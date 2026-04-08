import json


def save_results(results, path):
    with open(path, "w") as f:
        json.dump(results, f, indent=4)


def print_results(results):
    print("\n=== ANOMALIES DETECTED ===")

    if not results:
        print("No anomalies found.")
        return

    for r in results:
        print(f"\nIP: {r['ip']}")
        print(f"Requests: {r['requests']}")
        print(f"Failed logins: {r['failed_logins']}")
        print(f"Description: {r['description']}")