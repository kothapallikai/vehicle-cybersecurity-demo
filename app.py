import streamlit as st
import pandas as pd
import numpy as np
import time
import random
from datetime import datetime

# Set up the Streamlit page configuration
st.set_page_config(page_title="Global Vehicle IDPS Dashboard", layout="wide")
st.title("🚗 Global Vehicle Cybersecurity Simulation Dashboard")
st.markdown("**A demonstration of real-time vehicle monitoring, cyber attack detection, and prevention with IDPS and Quantum Security Integration**")

# Sidebar: User Inputs
st.sidebar.header("User Inputs")
num_vehicles = st.sidebar.number_input("Number of Vehicles", min_value=1, max_value=1000, value=5)
simulate_attack = st.sidebar.checkbox("Simulate Cyber Attack")

# Function to simulate vehicle data
def generate_vehicle_data(num):
    vehicle_data = pd.DataFrame({
        "Vehicle ID": [f"V-{i}" for i in range(1, num + 1)],
        "Country": random.choices(["USA", "Germany", "India", "China", "Brazil"], k=num),
        "Speed (km/h)": np.random.randint(50, 150, size=num),
        "RPM": np.random.randint(1000, 6000, size=num),
        "Status": ["Normal"] * num
    })
    return vehicle_data

# Function to simulate anomalies
def introduce_anomalies(data):
    num_anomalies = random.randint(1, len(data))
    anomaly_indices = random.sample(range(len(data)), num_anomalies)
    for idx in anomaly_indices:
        data.at[idx, "Status"] = "Anomalous"
    return data

# Main Dashboard
if st.button("Run Simulation"):
    with st.spinner('Running simulation...'):
        # Generate vehicle data
        vehicle_data = generate_vehicle_data(num_vehicles)
        
        # Simulate cyber attack if checkbox is selected
        if simulate_attack:
            vehicle_data = introduce_anomalies(vehicle_data)
            st.error("🚨 Cyber Attack Detected!")
            st.info("Alert sent to VSOC for further analysis.")
        
        # Display Real-Time Vehicle Data
        st.header("🚘 Real-Time Vehicle Data")
        st.dataframe(vehicle_data, width=700)
        
        # Display Detected Anomalies
        st.header("⚠️ Detected Anomalies")
        anomalies = vehicle_data[vehicle_data["Status"] == "Anomalous"]
        if not anomalies.empty:
            st.warning(f"{len(anomalies)} anomalies detected globally.")
            st.dataframe(anomalies)
        else:
            st.success("No anomalies detected.")
        
        # Incident Timeline
        st.header("🕒 Incident Timeline")
        timeline_data = [
            {"Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Event": "Vehicles Connected to IDPS"},
            {"Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Event": "Cyber Attack Detected" if simulate_attack else "No Cyber Attack"},
            {"Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Event": "Anomalies Sent to VSOC" if simulate_attack else "No Anomalies"},
            {"Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Event": "OTA Update Deployed"},
            {"Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Event": "Quantum Security Integration Planned"},
        ]
        timeline_df = pd.DataFrame(timeline_data)
        st.table(timeline_df)
        
        # OTA Update Deployment
        st.header("🚀 OTA Update Deployment")
        st.info("Deploying OTA Update to Secure All Vehicles...")
        time.sleep(2)
        st.success("✅ OTA Update Deployed Successfully!")
        
        # Quantum Security Integration
        st.header("🔒 Quantum Security Integration")
        st.info("Integrating Quantum Technology for Enhanced Security...")
        time.sleep(2)
        st.success("🔒 Quantum Security Successfully Integrated!")
else:
    st.info("Click the 'Run Simulation' button to start the IDPS demo.")

# Footer
st.markdown("---")
st.markdown("**Developed for showcasing global vehicle cybersecurity monitoring and prevention using advanced IDPS and quantum technology.**")
