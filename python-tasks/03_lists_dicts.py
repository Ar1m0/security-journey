# ports = [22, 80, 443]

# len(ports)

# ports[0]

# ports[-1]

# ports.append(8080)
# print(ports)
# ports.remove(80)
# print(ports)
# del ports[0]
# print(ports)
# print(80 in ports)
# print(443 in ports)
# print(ports)
# print(ports)
# print(ports)

# for port in ports:
#     print(port);

# alert = {
#     "rule": "SSH brute force",
#     "source_ip": "127.0.0.1",
#     "severity": "high",
#     "events": 47
# }

# print(alert["rule"])

# print(alert.get("events"))
# print(alert.get("dst_ip", "unknown"))
# alert["zalupa"] = "hui"
# print(alert)
# alert["events"] = alert["events"] + 1
# print(alert)
# del alert["events"]
# print(alert)

# print("hui" in alert)

# print(alert.values())

# for key, value in alert.items():
#     print(f"{key} = {value}")


# alert2 = {
#     "source": {
#         "ip": "203.0.113.45",
#         "port": 88
#     }
# }

# alert2["source"]["port"]

# alerts = [
#     {"rule": "SSH brute force", "ip": "203.0.113.45", "severity": "high"},
#     {"rule": "Port scan",       "ip": "198.51.100.7",  "severity": "medium"},
#     {"rule": "SSH brute force", "ip": "203.0.113.45", "severity": "high"},
# ]

# for a in alerts:
#     print (a["rule"], a["ip"]);

# high = [a for a in alerts if a["severity"] == "high"]

# from collections import Counter
# ip_counts = Counter(a["ip"] for a in alerts)

# ip_counts.most_common(1)


alerts = [
    {"rule": "DDoS attack", {}}
]