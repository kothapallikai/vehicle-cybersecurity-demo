import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime
import random

try:
    # Set up the Streamlit page configuration
    st.set_page_config(page_title="Global Vehicle IDPS Dashboard", layout="wide")
    st.title("🚗 Global Vehicle Cybersecurity Simulation Dashboard")
    st.markdown("**A demonstration of real-time vehicle monitoring, cyber attack detection, and prevention with IDPS and Quantum Security Integration**")

    # Sidebar: Global Metrics
    st.sidebar.header("🌍 Global Metrics")
    st.sidebar.metric(label="Connected Vehicles", value=f"{random.randint(900000, 1000000):,}")
    st.sidebar.metric(label="Active Anomalies", value=random.randint(5, 50))
    st.sidebar.metric(label="Countries Covered", value=random.randint(50, 150))

    # Main Dashboard
    col1, col2, col3 = st.columns(3)

    # Column 1: Real-Time Vehicle Data
    with col1:
        st.header("🚘 Real-Time Vehicle Data")
        vehicle_data = pd.DataFrame({
            "Vehicle ID": [f"V-{i}" for i in range(1, 6)],
            "Country": random.choices(["USA", "Germany", "India", "China", "Brazil"], k=5),
            "Speed (km/h)": np.random.randint(50, 150, size=5),
            "RPM": np.random.randint(1000, 6000, size=5),
            "Status": [random.choice(["Normal", "Anomalous"]) for _ in range(5)],
        })
        st.dataframe(vehicle_data, width=700)

    # Column 2: Anomaly Detection
    with col2:
        st.header("⚠️ Detected Anomalies")
        anomalies = vehicle_data[vehicle_data["Status"] == "Anomalous"]
        if not anomalies.empty:
            st.warning(f"{len(anomalies)} anomalies detected globally.")
            st.dataframe(anomalies)
        else:
            st.success("No anomalies detected.")

    # Column 3: Cyber Attack Simulation
    with col3:
        st.header("💥 Cyber Attack Simulation")
        attack_types = ["SQL Injection", "Spoofing Attack", "DoS Attack", "Malware Injection"]
        if st.button("Simulate Cyber Attack"):
            attack = random.choice(attack_types)
            st.error(f"🚨 Cyber Attack Detected: {attack}")
            st.info("Alert sent to VSOC for further analysis.")

    # Incident Timeline
    st.header("🕒 Incident Timeline")
    timeline_data = [
        {"Time": "2025-02-01 10:00:00", "Event": "Vehicles Connected to IDPS"},
        {"Time": "2025-02-01 10:30:00", "Event": "Cyber Attack Detected"},
        {"Time": "2025-02-01 10:35:00", "Event": "Anomalies Sent to VSOC"},
        {"Time": "2025-02-01 10:50:00", "Event": "OTA Update Deployed"},
        {"Time": "2025-02-01 11:00:00", "Event": "Quantum Security Integration Planned"},
    ]
    timeline_df = pd.DataFrame(timeline_data)
    st.table(timeline_df)

    # OTA Update Deployment
    st.header("🚀 OTA Update Deployment")
    if st.button("Deploy OTA Update"):
        st.info("Deploying OTA Update to Secure All Vehicles...")
        time.sleep(2)
        st.success("✅ OTA Update Deployed Successfully!")

    # Quantum Security Integration
    st.header("🔒 Quantum Security Integration")
    if st.button("Integrate Quantum Security"):
        st.info("Integrating Quantum Technology for Enhanced Security...")
        time.sleep(2)
        st.success("🔒 Quantum Security Successfully Integrated!")

    # Footer
    st.markdown("---")
    st.markdown("**Developed for showcasing global vehicle cybersecurity monitoring and prevention using advanced IDPS and quantum technology.")

except ModuleNotFoundError as e:
    st.error("ModuleNotFoundError: Some required modules are missing. Please ensure that all dependencies are installed.")
    st.write("Detailed Error:", str(e))
