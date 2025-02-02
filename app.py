import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import random
import time

# Set up the Streamlit page configuration
st.set_page_config(page_title="VicOne xCarbon and xNexus Demo", layout="wide")
st.title("🚗 VicOne xCarbon and xNexus Simulation Dashboard")
st.markdown("**Demonstration of real-time vehicle monitoring, cyberattack detection, IDPS activation, VSOC alerts, and OTA updates**")

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

# Generate initial vehicle data
vehicle_data = generate_vehicle_data(num_vehicles)

# Display the map with vehicle locations using custom car icons
st.header("🌍 Vehicle Locations")
icon_url = "https://img.icons8.com/ios-filled/50/000000/car.png"
icon_data = {
    "url": icon_url,
    "width": 242,
    "height": 242,
    "anchorY": 242
}
vehicle_data['icon_data'] = None
for i in vehicle_data.index:
    vehicle_data['icon_data'][i] = icon_data
vehicle_layer = pdk.Layer(
    type="IconLayer",
    data=vehicle_data,
    get_icon="icon_data",
    get_size=4,
    size_scale=15,
    get_position=["longitude", "latitude"],
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
    vehicle_data = simulate_cyber_attack(vehicle_data)
    st.warning("Cyberattack simulated!")

    # Activate IDPS
    detected_attacks = activate_idps_system(vehicle_data)
    if not detected_attacks.empty:
        st.error(f"{len(detected_attacks)} attacks detected!")
        st.dataframe(detected_attacks)
        st.info("Alerts sent to VSOC for further analysis.")
    else:
        st.success("No attacks detected.")

# Initiate OTA update
if st.button("Initiate OTA Update"):
    with st.spinner('Deploying OTA Update...'):
        time.sleep(2)
        st.success("OTA Update Deployed Successfully!")

# Footer
st.markdown("---")
st.markdown("**Developed to showcase the capabilities of VicOne's xCarbon and xNexus solutions.**")
