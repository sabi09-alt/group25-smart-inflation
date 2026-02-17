import streamlit as st
import joblib
import numpy as np
import os

# ---------------------------------------------------
# PAGE CONFIG (must be first Streamlit command)
# ---------------------------------------------------
st.set_page_config(
    page_title="Smart Inflation Forecasting System",
    page_icon="📊",
    layout="centered"
)

# ---------------------------------------------------
# BACKGROUND IMAGE + PROFESSIONAL STYLE
# ---------------------------------------------------
page_style = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1507679799987-c73779587ccf");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

.main {
    background: rgba(255, 255, 255, 0.90);
    padding: 2rem;
    border-radius: 15px;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-weight: bold;
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD MODEL SAFELY
# ---------------------------------------------------
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "model.pkl")
model = joblib.load(model_path)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.header("📘 About this App")
st.sidebar.info(
    """
    This app predicts inflation impact based on user inputs.

    Developed by **Group 25**
    """
)

# ---------------------------------------------------
# TITLE SECTION
# ---------------------------------------------------
st.title("📊 Smart Inflation Prediction System")
st.markdown(
    "Welcome to our **Smart Inflation Analysis App**. "
    "Enter economic indicators below to forecast inflation."
)

st.divider()

# ---------------------------------------------------
# INPUT SECTION (YOUR DATA – NOT REDUCED)
# ---------------------------------------------------
st.subheader("📥 Enter Economic Indicators")

gdp_growth = st.number_input(
    "📈 GDP Growth Rate (%)",
    min_value=-10.0,
    max_value=20.0,
    value=5.0
)

interest_rate = st.number_input(
    "🏦 Interest Rate (%)",
    min_value=0.0,
    max_value=30.0,
    value=10.0
)

exchange_rate = st.number_input(
    "💱 Exchange Rate (TZS per USD)",
    min_value=1000.0,
    max_value=5000.0,
    value=2500.0
)

unemployment = st.number_input(
    "👥 Unemployment Rate (%)",
    min_value=0.0,
    max_value=50.0,
    value=10.0
)

money_supply = st.number_input(
    "💰 Money Supply (M2)",
    min_value=0.0,
    value=1000.0
)

st.divider()

# ---------------------------------------------------
# PREDICTION SECTION
# ---------------------------------------------------
if st.button("🚀 Predict Inflation Rate"):

    input_data = np.array([[
        gdp_growth,
        interest_rate,
        exchange_rate,
        unemployment,
        money_supply
    ]])

    prediction = model.predict(input_data)

    st.success(f"📈 Predicted Inflation Rate: {prediction[0]:.2f}%")

    if prediction[0] < 5:
        st.info("Inflation is considered LOW and stable.")
    elif prediction[0] < 10:
        st.warning("Inflation is MODERATE.")
    else:
        st.error("Inflation is HIGH. Economic pressure may increase.")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.caption("© 2026 Group 25 | Smart Inflation Forecasting System")
