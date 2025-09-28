🌱 Sustainability Tracker – AI Copilot

The Sustainability Tracker is an interactive web app that helps individuals and organizations understand their environmental impact and adopt more eco-friendly practices.
It allows users to track activities like transportation, electricity consumption, diet, and waste management, while providing AI-powered recommendations for sustainable living.

✨ Features
📊 Dashboard: Visualize your daily sustainability metrics
🖼️ Interactive Learning: Click on images (transport, energy, water, waste) to explore eco-friendly tips
🤖 AI Recommendations: Get smart suggestions to reduce your carbon footprint
🔌 FastAPI Backend: Manages data and recommendation logic
🎨 Streamlit Frontend: Provides a simple and engaging user interface

🚀 Tech Stack
Backend: FastAPI
Frontend: Streamlit
Python Libraries: Requests, Pandas, Altair, etc.

⚡ Installation
1. Clone the repository
git clone https://github.com/MaripeddiNavya/Sustainability-Tracker-AI-Copilot
cd SustainabilityTracker

2. Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate   # (Windows)
source venv/bin/activate  # (Linux/Mac)

pip install -r requirements.txt
uvicorn backend.app:app --reload

3. Frontend Setup
cd ../frontend
pip install -r requirements.txt
streamlit run app.py

🎯 Purpose
This project aims to raise awareness about sustainability and show how small changes in daily life can make a big environmental impact.

🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit pull requests.
