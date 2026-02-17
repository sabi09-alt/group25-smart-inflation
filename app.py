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

st.write("---")


gdp_growth = st.number_input("GDP Growth Rate (%)", min_value=-10.0, max_value=20.0, value=5.0)
interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=30.0, value=10.0)
exchange_rate = st.number_input("Exchange Rate (TZS per USD)", min_value=1000.0, max_value=5000.0, value=2500.0)
unemployment = st.number_input("Unemployment Rate (%)", min_value=0.0, max_value=50.0, value=10.0)
money_supply = st.number_input("Money Supply (M2)", min_value=0.0, value=1000.0)


st.write("---")

if st.button("Predict Inflation Rate"):


if st.button("🚀 Predict Now"):
    # Prepare input data
    input_data = np.array([[gdp_growth, interest_rate, exchange_rate, unemployment,money_supply]])



    prediction = model.predict(input_data)

    st.success(f"Predicted Value: {prediction[0]:.2f}")

st.markdown("---")
st.caption("© 2026 Group 25 | Smart Inflation Project")
