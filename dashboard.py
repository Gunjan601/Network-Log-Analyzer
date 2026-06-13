import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Network Log Analyzer",layout="wide")

st.markdown("""
<style>

.main{
    background-color: white;
}

h1{
    color: #1f2937;
    text-align: center;
    border-bottom: 3px solid #2563eb;
    padding-bottom: 10px;
}

h2{
    color: #374151;
    border-left: 5px solid #2563eb;
    padding-left: 10px;
}

div[data-testid="metric-container"]{
    background-color: white;
    border: 2px solid #e5e7eb;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# TITLE

st.title("🛡️ Network Log Analyzer")

st.markdown("### Security Monitoring Dashboard")

st.markdown("---")

# LOAD DATA

try:
    alerts_df = pd.read_csv("reports/alerts.csv")
    total_alerts = len(alerts_df)
except:
    total_alerts = 0
    alerts_df = pd.DataFrame()

try:
    attackers_df = pd.read_csv("reports/attack_stats.csv")
except:
    attackers_df = pd.DataFrame()

try:
    ports_df = pd.read_csv("reports/ports.csv")
except:
    ports_df = pd.DataFrame()

try:
    attack_types_df = pd.read_csv("reports/attack_types.csv")
except:
    attack_types_df = pd.DataFrame()

# METRICS

col1, col2, col3 = st.columns(3)

with col1:
    st.metric( "Total Alerts",total_alerts)

with col2:
    st.metric("Attacker IPs",len(attackers_df))

with col3:
    st.metric("Targeted Ports",len(ports_df))

st.markdown("---")

# TOP ATTACKER IPS

st.subheader("Top Attacker IPs")

if not attackers_df.empty:

    fig = px.bar(
        attackers_df,
        x="IP",
        y="Attacks",
        title="Top Attacker IPs"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# TARGETED PORTS

st.subheader("Most Targeted Ports")

if not ports_df.empty:

    fig2 = px.bar(
        ports_df,
        x="Port",
        y="Hits",
        title="Most Targeted Ports"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ATTACK TYPES

st.subheader("Attack Types")

if not attack_types_df.empty:

    fig3 = px.pie(
        attack_types_df,
        names="Attack Type",
        values="Count",
        title="Attack Type Distribution"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

#RECENT ALERTS
st.subheader("Recent Alerts")

if not alerts_df.empty:

    st.dataframe(
        alerts_df.tail(10),
        use_container_width=True
    )

else:

    st.write("No alerts available.")

# SIDEBAR
with st.sidebar:

    st.title(" Dashboard")

    st.write("Network Security Monitoring")

    st.markdown("---")

    st.write(f"Total Alerts: {total_alerts}")

    st.write(f"Attacker IPs: {len(attackers_df)}")

    st.write(f"Targeted Ports: {len(ports_df)}")