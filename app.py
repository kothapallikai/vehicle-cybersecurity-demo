import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import random
import time

# Set up the Streamlit page configuration
st.set_page_config(page_title="IDPS Demo Dashboard", layout="wide")
st.title("🚗 Intrusion Detection and Prevention System (IDPS) Demo Dashboard")
st.markdown("**Real-time vehicle monitoring, cyberattack detection, IDPS activation, VSOC alerts, and OTA updates**")

# Initialize session state for vehicle data and alerts
if 'vehicle_data' not in st.session_state:
    st.session_state.vehicle_data = pd.DataFrame()
if 'vsoc_alerts' not in st.session_state:
    st.session_state.vsoc_alerts = pd.DataFrame()

# Sidebar: User Inputs
st.sidebar.header("User Inputs")
num_vehicles = st.sidebar.slider("Number of Vehicles", min_value=10, max_value=500, value=100, step=10)

# Function to generate random vehicle data
def generate_vehicle_data(num):
    data = pd.DataFrame({
        'latitude': np.random.uniform(-90, 90, num),
        'longitude': np.random.uniform(-180, 180, num),
        'Vehicle ID': [f"V-{i}" for i in range(1, num + 1)],
        'Status': ['Normal'] * num
    })
    return data

# Function to simulate cyberattacks
def simulate_cyber_attack(data):
    attack_types = ["SQL Injection", "Spoofing Attack", "DoS Attack", "Malware Injection"]
    num_attacks = random.randint(1, len(data) // 10)
    attack_indices = random.sample(range(len(data)), num_attacks)
    for idx in attack_indices:
        data.at[idx, 'Status'] = random.choice(attack_types)
    return data

# Function to activate IDPS
def activate_idps_system(data):
    detected_attacks = data[data['Status'] != 'Normal']
    return detected_attacks

# Generate initial vehicle data if not already generated
if st.session_state.vehicle_data.empty:
    st.session_state.vehicle_data = generate_vehicle_data(num_vehicles)

# Display the map with vehicle locations as red dots
st.header("🌍 Vehicle Locations")
vehicle_layer = pdk.Layer(
    'ScatterplotLayer',
    data=st.session_state.vehicle_data,
    get_position='[longitude, latitude]',
    get_fill_color='[255, 0, 0, 160]',
    get_radius=200000,
    pickable=True
)
view_state = pdk.ViewState(
    latitude=0,
    longitude=0,
    zoom=1
)
r = pdk.Deck(
    layers=[vehicle_layer],
    initial_view_state=view_state,
    tooltip={"text": "{Vehicle ID}"}
)
st.pydeck_chart(r)

# Simulate cyberattack
if st.button("Simulate Cyberattack"):
    st.session_state.vehicle_data = simulate_cyber_attack(st.session_state.vehicle_data)
    st.warning("Cyberattack simulated!")

    # Activate IDPS
    detected_attacks = activate_idps_system(st.session_state.vehicle_data)
    if not detected_attacks.empty:
        st.error(f"{len(detected_attacks)} attacks detected!")

        # Update VSOC Alerts in session state
        st.session_state.vsoc_alerts = detected_attacks[['Vehicle ID', 'Status']]

        # Display VSOC Alerts
        st.subheader("📡 VSOC Alerts")
        st.dataframe(st.session_state.vsoc_alerts)

        # OTA Updates Visualization
        if st.button("Initiate OTA Update"):
            with st.spinner('Deploying OTA Update...'):
                time.sleep(2)
                st.success("OTA Update Deployed Successfully!")

        # IDPS Rule Set Update
        if st.button("Update IDPS Rule Set"):
            with st.spinner('Updating IDPS Rule Set...'):
                time.sleep(2)
                st.success("IDPS Rule Set Updated Successfully!")
    else:
        st.success("No attacks detected.")

# Display VSOC Alerts if they exist
if not st.session_state.vsoc_alerts.empty:
    st.subheader("📡 VSOC Alerts")
    st.dataframe(st.session_state.vsoc_alerts)

# Footer
st.markdown("---")
st.markdown("**Developed to demonstrate an advanced IDPS with real-time monitoring and response capabilities.**")
