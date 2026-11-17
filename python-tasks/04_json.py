import json

with open("sample_alert.json", "r", encoding="utf-8") as f:
    alert = json.load(f)

print(alert["rule"])
print(alert["source_ip"])
print(alert["tags"])
print(alert["events"] > 20)

print(alert.get("severity", "unknown"))
print(alert.get("nonexistent", "n/a"))


report = {
    "generated_at": "2025-11-16",
    "source": "auth.log",
    "failed_logins": 47,
    "unique_ips": 3,
    "top_ip": "203.0.113.45"
}

with open("report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2, ensure_ascii=False)


alerts = [
    {"rule": "SSH brute force", "ip": "203.0.113.45", "severity": "high"},
    {"rule": "Port scan",       "ip": "198.51.100.7",  "severity": "medium"},
    {"rule": "SSH brute force", "ip": "203.0.113.45", "severity": "high"},
]

high = [a for a in alerts if a["severity"] == "high"]
print(len(high))

from collections import Counter
ips = Counter(a["ip"] for a in alerts)
print(ips.most_common(1))