threat_scores = {}


def add_score(ip, score):

    if ip not in threat_scores:
        threat_scores[ip] = 0

    threat_scores[ip] += score


def show_scores():

    print("\n===== THREAT SCORES =====\n")

    for ip, score in threat_scores.items():

        if score <= 30:
            level = "LOW"

        elif score <= 70:
            level = "MEDIUM"

        else:
            level = "HIGH"

        print(f"{ip} -> Score: {score} ({level})")