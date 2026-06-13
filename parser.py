import re

def parse_log(line):

    log_data = {}

    timestamp = re.search(
        r'([A-Z][a-z]{2}\s+\d+\s+\d+:\d+)',
        line
    )

    ip = re.search(
        r'(\d+\.\d+\.\d+\.\d+)',
        line
    )

    port = re.search(
        r'port\s+(\d+)',
        line
    )

    username = re.search(
        r'for\s+(\w+)',
        line
    )

    if timestamp:
        log_data["timestamp"] = timestamp.group(1)

    if ip:
        log_data["ip"] = ip.group(1)

    if port:
        log_data["port"] = int(port.group(1))

    if username:
        log_data["username"] = username.group(1)

    if "Failed password" in line:
        log_data["event"] = "failed_login"

    elif "Connection attempt" in line:
        log_data["event"] = "connection_attempt"

    return log_data