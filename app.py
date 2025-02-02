import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# Set up the Streamlit page configuration
st.set_page_config(page_title="Global Vehicle IDPS Dashboard", layout="wide")
st.title("🚗 Global Vehicle Cybersecurity Simulation Dashboard")
st.markdown("**A demonstration of real-time vehicle monitoring, cyber attack detection, and prevention with IDPS and Quantum Security Integration**")

# Sidebar: User Inputs
st.sidebar.header("User Inputs")
num_vehicles = st.sidebar.slider("Number of Vehicles", min_value=10, max_value=1000, value=100, step=10)

# Function to generate random vehicle data
def generate_vehicle_data(num):
    data = pd.DataFrame({
        'latitude': np.random.uniform(-90, 90, num),
        'longitude': np.random.uniform(-180, 180, num),
        'Vehicle ID': [f"V-{i}" for i in range(1, num + 1)],
        'Status': ['Normal'] * num
    })
    return data

# Function to simulate cyber attacks
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

# Generate initial vehicle data
vehicle_data = generate_vehicle_data(num_vehicles)

# Display the map with vehicle locations
st.header("🌍 Vehicle Locations")
st.map(vehicle_data[['latitude', 'longitude']])

# Simulate cyber attack if button is pressed
if st.button("Simulate Cyber Attack"):
    vehicle_data = simulate_cyber_attack(vehicle_data)
    st.warning("Cyber attack simulated!")

# Activate IDPS if button is pressed
if st.button("Activate IDPS"):
    detected_attacks = activate_idps_system(vehicle_data)
    if not detected_attacks.empty:
        st.error(f"{len(detected_attacks)} attacks detected!")
        st.dataframe(detected_attacks)
        st.info("Alerts sent to VSOC for further analysis.")
    else:
        st.success("No attacks detected.")

# Initiate OTA update if button is pressed
if st.button("Initiate OTA Update"):
    with st.spinner('Deploying OTA Update...'):
        time.sleep(2)
        st.success("OTA Update Deployed Successfully!")

# Footer
st.markdown("---")
st.markdown("**Developed for showcasing global vehicle cybersecurity monitoring and prevention using advanced IDPS and quantum technology.**")
