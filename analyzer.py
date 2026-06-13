from parser import parse_log
from detections import process_log
from detections import generate_alerts
from threat_scoring import show_scores
from attack_statistics import show_statistics
from attack_statistics import export_statistics
from attack_statistics import export_ports
from attack_statistics import export_attack_types

LOG_FILE = "logs/sample.log"

with open(LOG_FILE, "r") as file:
    logs = file.readlines()

for line in logs:

    parsed_log = parse_log(line)

    process_log(parsed_log)

generate_alerts()
show_scores()
show_statistics()
export_statistics()
export_ports()
export_attack_types()