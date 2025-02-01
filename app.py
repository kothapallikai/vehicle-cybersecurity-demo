import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from PIL import Image
import time
import random

# Set page configuration
st.set_page_config(page_title="Vehicle Cybersecurity Demo", layout="wide")

# Load dummy car image
st.title("🚗 Vehicle Cybersecurity Simulation Dashboard")
st.markdown("**Real-time Vehicle Monitoring with Cybersecurity Insights**")
car_image_url = "https://via.placeholder.com/600x300.png?text=Car+Simulation"  # Replace with your hosted image URL
st.image(car_image_url, caption="Vehicle Simulation", use_column_width=True)

# Sidebar: Threat Levels
st.sidebar.header("📊 Threat Levels")
st.sidebar.metric(label="Connected Vehicles", value="926,727")
st.sidebar.metric(label="Cyber Incidents", value=random.randint(1, 20))
st.sidebar.metric(label="Mobility Incidents", value=random.randint(0, 5))

# Main Dashboard
col1, col2, col3 = st.columns(3)

with col1:
    st.header("🚨 Detected Anomalies")
    anomaly_types = ["SQL Injection", "Spoofing", "DoS Attack", "Malware Injection"]
    detected_anomaly = random.choice(anomaly_types)
    st.warning(f"Latest Threat: {detected_anomaly}")
    st.write("Threat detected at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

with col2:
    st.header("📡 Real-Time Vehicle Data")
    data = {
        "Vehicle ID": [f"V-{i}" for i in range(1, 6)],
        "Speed (km/h)": np.random.randint(0, 120, 5),
        "RPM": np.random.randint(500, 7000, 5),
        "Status": [random.choice(["Normal", "Anomalous"]) for _ in range(5)],
    }
    vehicle_data = pd.DataFrame(data)
    st.dataframe(vehicle_data)

with col3:
    st.header("🔄 OTA Updates")
    if st.button("Deploy OTA Patch"):
        st.info("🚀 Deploying OTA Update...")
        time.sleep(2)
        st.success("✅ OTA Patch Deployed Successfully!")

# Incident Tracking
st.header("🛠️ Incident Timeline")
timeline_data = [
    {"Time": "2025-02-01 12:00:00", "Incident": "SQL Injection detected"},
    {"Time": "2025-02-01 12:05:00", "Incident": "Alert sent to VSOC"},
    {"Time": "2025-02-01 12:10:00", "Incident": "VSOC identified threat"},
    {"Time": "2025-02-01 12:15:00", "Incident": "OTA Patch Initiated"},
    {"Time": "2025-02-01 12:20:00", "Incident": "IDPS Ruleset Updated"},
]
timeline_df = pd.DataFrame(timeline_data)
st.table(timeline_df)

# Footer: Quantum Security
st.header("🔒 Quantum Security")
if st.button("Integrate Quantum Security"):
    st.info("🔒 Integrating Quantum Security...")
    time.sleep(2)
    st.success("Quantum Security Measures Implemented!")
