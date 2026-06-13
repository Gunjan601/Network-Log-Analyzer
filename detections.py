from collections import defaultdict
from threat_scoring import add_score
from alerts import generate_alert
from attack_statistics import (
    record_attack,
    record_port,
    record_alert
)

failed_logins = defaultdict(int)
port_activity = defaultdict(set)

BRUTE_FORCE_THRESHOLD = 5
PORT_SCAN_THRESHOLD = 4


def process_log(log):

    ip = log.get("ip")

    if not ip:
        return

    if log.get("event") == "failed_login":
        failed_logins[ip] += 1
        record_attack(ip,"failed_login")
        add_score(ip, 10)
        if failed_logins[ip] >= BRUTE_FORCE_THRESHOLD:
            generate_alert(f"Possible brute force attack from {ip}","HIGH")
            record_alert()
        
        

    if "port" in log:
        port_activity[ip].add(log["port"])
        record_port(log["port"])


def generate_alerts():

    print("\n===== BRUTE FORCE ANALYSIS =====\n")

    for ip, attempts in failed_logins.items():

        print(f"{ip} -> Failed Attempts: {attempts}")

        if attempts >= BRUTE_FORCE_THRESHOLD:
            generate_alert(f"Possible brute force attack from {ip}","HIGH")

    print("\n===== PORT SCAN ANALYSIS =====\n")

    for ip, ports in port_activity.items():

        print(f"{ip} -> Accessed Ports: {sorted(ports)}")

        if len(ports) >= PORT_SCAN_THRESHOLD:
            add_score(ip, 30)
            generate_alert(f"Possible port scan detected from {ip}","MEDIUM")
            record_alert()