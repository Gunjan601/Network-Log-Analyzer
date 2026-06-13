# Network Log Analyzer

A Python-based IDS-style network monitoring and log analysis system.

## Features

- Log Parsing
- Failed Login Detection
- Brute Force Detection
- Port Scan Detection
- Threat Scoring
- Real-Time Monitoring
- Alert Generation
- CSV Reporting
- Streamlit Dashboard

## Technologies

- Python
- Streamlit
- Pandas
- Plotly

## Run

python analyzer.py

streamlit run dashboard.py

## Note 
analyzer.py works on the whole existing log file and contains features such as threat scoring.
realtime_monitor.py is for realtime monitoring of every new event entered into the log file.

## Future developments that can be added
- IP blocking feature.
- Threat intelligence feeds.
- threat hunting.
