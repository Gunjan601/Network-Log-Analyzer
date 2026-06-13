from collections import defaultdict
import pandas as pd

# Total attacks per IP
attacker_ips = defaultdict(int)

# Port hit counts
targeted_ports = defaultdict(int)

# Event counts
attack_types = defaultdict(int)

# Total alerts
total_alerts = 0


def record_attack(ip, event_type):

    attacker_ips[ip] += 1

    attack_types[event_type] += 1


def record_port(port):

    targeted_ports[port] += 1


def record_alert():

    global total_alerts

    total_alerts += 1


def show_statistics():

    print("\n===== STATISTICS =====\n")

    print(f"Total Alerts: {total_alerts}")

    print("\nTop Attacker IPs:")

    for ip, count in sorted(
            attacker_ips.items(),
            key=lambda x: x[1],
            reverse=True):

        print(f"{ip} -> {count}")

    print("\nMost Targeted Ports:")

    for port, count in sorted(
            targeted_ports.items(),
            key=lambda x: x[1],
            reverse=True):

        print(f"Port {port} -> {count}")

    print("\nAttack Types:")

    for attack, count in attack_types.items():

        print(f"{attack} -> {count}")

def get_total_alerts():
    return total_alerts


def get_top_attackers():
    return dict(attacker_ips)


def get_ports():
    return dict(targeted_ports)


def get_attack_types():
    return dict(attack_types)

def export_statistics():

    data = []

    for ip, attacks in attacker_ips.items():

        data.append({
            "IP": ip,
            "Attacks": attacks
        })

    df = pd.DataFrame(data)

    df.to_csv(
        "reports/attack_stats.csv",
        index=False
    )

def export_ports():

    import pandas as pd

    data = []

    for port, hits in targeted_ports.items():

        data.append({
            "Port": port,
            "Hits": hits
        })

    df = pd.DataFrame(data)

    df.to_csv(
        "reports/ports.csv",
        index=False
    )

def export_attack_types():

    import pandas as pd

    data = []

    for attack_type, count in attack_types.items():

        data.append({
            "Attack Type": attack_type,
            "Count": count
        })

    df = pd.DataFrame(data)

    df.to_csv(
        "reports/attack_types.csv",
        index=False
    )