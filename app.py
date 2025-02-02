import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import random
import time
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations from a URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations
satellite_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_j1adxtyb.json")
alert_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_tutvdkg0.json")

# Set up the Streamlit page configuration
st.set_page_config(page_title="Global Vehicle IDPS Dashboard", layout="wide")
st.title("🚗 Global Vehicle Cybersecurity Simulation Dashboard")
st.markdown("**A demonstration of real-time vehicle monitoring, cyber attack detection, prevention with IDPS, and OTA updates**")

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

# Display the map with vehicle locations using custom car icons
st.header("🌍 Vehicle Locations")
icon_url = "https://img.icons8.com/ios-filled/50/000000/car.png"
icon_data = {
    "url": icon_url,
    "width": 242,
    "height": 242,
    "anchorY": 242
}
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

# Simulate cyber attack
vehicle_data = simulate_cyber_attack(vehicle_data)
st.warning("Cyber attack simulated!")

# Activate IDPS
detected_attacks = activate_idps_system(vehicle_data)
if not detected_attacks.empty:
    st.error(f"{len(detected_attacks)} attacks detected!")
    st.dataframe(detected_attacks)
    st.info("Alerts sent to VSOC for further analysis.")
    st_lottie(alert_animation, height=200, key="alert")
else:
    st.success("No attacks detected.")

# Initiate OTA update
if st.button("Initiate OTA Update"):
    st_lottie(satellite_animation, height=300, key="satellite")
    with st.spinner('Deploying OTA Update...'):
        time.sleep(2)
        st.success("OTA Update Deployed Successfully!")

# Footer
st.markdown("---")
st.markdown("**Developed for showcasing global vehicle cybersecurity monitoring and prevention using advanced IDPS technology.**")
