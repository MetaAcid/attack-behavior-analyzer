import matplotlib.pyplot as plt


def save_anomaly_plot(df, output_path):
    normal = df[df["prediction"] == "NORMAL"]
    anomaly = df[df["prediction"] == "ANOMALY"]

    plt.figure(figsize=(10, 6))
    plt.scatter(normal["requests"], normal["failed_logins"], alpha=0.7, label="Normal")
    plt.scatter(anomaly["requests"], anomaly["failed_logins"], alpha=0.9, label="Anomaly")

    plt.xlabel("Requests")
    plt.ylabel("Failed Logins")
    plt.title("Attack Behavior Analysis")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()