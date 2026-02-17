import streamlit as st
import joblib
import pandas as pd
import os

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="Smart Inflation system",
    page_icon="📈",
    layout="centered"
)

# ---------------------------------------------------
# Background Image CSS
# ---------------------------------------------------
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1559526324-4b87b5e36e44");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

.main {
    background: rgba(255, 255, 255, 0.85);
    padding: 2rem;
    border-radius: 15px;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "model.pkl")
model = joblib.load(model_path)

# ---------------------------------------------------
# App Content
# ---------------------------------------------------
st.title("📊 Smart Inflation Predictor")
st.markdown("### Developed by Group 25")

st.write("Enter the economic indicators below:")

inflation = st.number_input("Inflation Rate (%)", 0.0, 100.0, 5.0)
gdp = st.number_input("GDP Growth (%)", -50.0, 50.0, 3.0)

if st.button("🚀 Predict Now"):
    input_data = pd.DataFrame({
        "inflation": [inflation],
        "gdp": [gdp]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Value: {prediction[0]:.2f}")

st.markdown("---")
st.caption("© 2026 Group 25 | Smart Inflation Project")
