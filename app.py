import streamlit as st
import os
import requests

st.set_page_config(page_title="🌱 Sustainability Tracker – AI Copilot", layout="wide")

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
API_URL = "http://127.0.0.1:8000/calculate"

# ----------------- Topics -----------------
topics = {
    "Carbon Footprint": {
        "image": os.path.join(IMAGES_DIR, "carbon_footprint.png"),
        "extra_image": os.path.join(IMAGES_DIR, "carbon_extra.png"),
        "description": "🌍 Tracks CO₂ from driving, electricity, diet, and waste using Azure AI and ML.",
        "color": "#FFADAD"
    },
    "Water Usage": {
        "image": os.path.join(IMAGES_DIR, "water_usage.png"),
        "extra_image": os.path.join(IMAGES_DIR, "water_extra.png"),
        "description": "💧 Tracks water consumption and provides actionable recommendations.",
        "color": "#ADE8F4"
    },
    "Energy Saving": {
        "image": os.path.join(IMAGES_DIR, "energy_saving.png"),
        "extra_image": os.path.join(IMAGES_DIR, "energy_extra.png"),
        "description": "💡 Monitors electricity usage and suggests energy-efficient habits.",
        "color": "#FFD6A5"
    },
    "Waste Management": {
        "image": os.path.join(IMAGES_DIR, "waste_management.png"),
        "extra_image": os.path.join(IMAGES_DIR, "waste_extra.png"),
        "description": "♻️ Helps minimize waste and supports recycling and composting practices.",
        "color": "#CAFFBF"
    }
}

if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = None

# ----------------- Header -----------------
st.markdown("<h1 style='text-align: center;'>🌱 Sustainability Tracker – AI Copilot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Click a topic or enter daily activities to estimate carbon footprint and get recommendations.</p>", unsafe_allow_html=True)
st.markdown("---")

# ----------------- Functions -----------------
def show_topics():
    cols = st.columns(2)
    for i, (topic, data) in enumerate(topics.items()):
        with cols[i % 2]:
            st.markdown(
                f"<div style='background-color:{data['color']}; padding:15px; border-radius:10px; text-align:center'><h3>{topic}</h3></div>",
                unsafe_allow_html=True
            )
            if os.path.exists(data["image"]):
                if st.button(f"Explore {topic}", key=topic):
                    st.session_state.selected_topic = topic
                st.image(data["image"], width=200)
            else:
                st.warning(f"Image not found: {data['image']}")

def show_topic_detail(topic):
    data = topics[topic]
    st.button("⬅️ Back to Topics", on_click=lambda: st.session_state.update({"selected_topic": None}))
    st.markdown(f"<h2 style='color:{data['color']}'>{topic}</h2>", unsafe_allow_html=True)
    st.write(data["description"])
    if os.path.exists(data["extra_image"]):
        st.image([data["image"], data["extra_image"]], use_container_width=True, width=300)
    else:
        st.image(data["image"], use_container_width=True, width=300)

# ----------------- Activity Input -----------------
st.markdown("---")
st.subheader("📝 Enter Your Daily Activities")
with st.form("activity_form"):
    km_driven = st.number_input("Distance traveled by car (km)", min_value=0.0, value=0.0)
    electricity_kwh = st.number_input("Electricity used at home (kWh)", min_value=0.0, value=0.0)
    meat_meals = st.number_input("Number of meat-based meals", min_value=0, value=0)
    waste_kg = st.number_input("Waste generated (kg)", min_value=0.0, value=0.0)
    water_liters = st.number_input("Water used (liters)", min_value=0.0, value=0.0)
    energy_usage_kwh = st.number_input("Other energy usage (kWh)", min_value=0.0, value=0.0)
    submitted = st.form_submit_button("Calculate Carbon Footprint")

if submitted:
    payload = {
        "km_driven": km_driven,
        "electricity_kwh": electricity_kwh,
        "meat_meals": meat_meals,
        "waste_kg": waste_kg,
        "water_liters": water_liters,
        "energy_usage_kwh": energy_usage_kwh
    }
    try:
        response = requests.post(API_URL, json=payload).json()
        emissions = response.get("emissions", {})
        total_carbon = response.get("total_carbon", 0)
        recs = response.get("recommendations", {})
        overall_recs = response.get("overall_recommendations", [])

        st.subheader("🌿 Category-wise Carbon Footprint")
        for cat, val in emissions.items():
            st.metric(cat, f"{val} kg CO₂")

        st.subheader("🌍 Total Carbon Footprint")
        st.metric("Total CO₂ Emissions (kg)", total_carbon)

        st.subheader("💡 Recommendations by Category")
        for cat, rec in recs.items():
            st.markdown(f"**{cat}:** {rec}")

        st.subheader("📝 Overall Recommendation")
        for rec in overall_recs:
            st.markdown(f"- {rec}")

    except Exception as e:
        st.error(f"Could not calculate emissions: {e}")

# ----------------- Display Topics -----------------
if st.session_state.selected_topic is None:
    show_topics()
else:
    show_topic_detail(st.session_state.selected_topic)
