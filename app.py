import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Group 25 – Smart Inflation",
    page_icon="📈",
    layout="wide"
)

# ---------------------------------------------------
# Load Model Safely
# ---------------------------------------------------
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "model.pkl")
model = joblib.load(model_path)

# ---------------------------------------------------
# Header Section
# ---------------------------------------------------
st.title("📊 Smart Inflation Prediction System")
st.markdown("""
Welcome to our **Smart Inflation Analysis App**.  
Enter the economic indicators below and click **Predict** to see the result.
""")

st.divider()

# ---------------------------------------------------
# Sidebar Information
# ---------------------------------------------------
st.sidebar.header("📘 About This App")
st.sidebar.info("""
This application predicts economic outcomes based on selected indicators.

Developed by **Group 25**  
Powered by Machine Learning 🚀
""")

# ---------------------------------------------------
# Main Layout (Columns)
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Input Economic Data")

    inflation = st.number_input(
        "Inflation Rate (%)",
        min_value=0.0,
        max_value=100.0,
        value=5.0
    )

    gdp = st.number_input(
        "GDP Growth (%)",
        min_value=-50.0,
        max_value=50.0,
        value=3.0
    )

with col2:
    st.subheader("📌 Current Inputs")
    st.write(f"Inflation Rate: **{inflation}%**")
    st.write(f"GDP Growth: **{gdp}%**")

st.divider()

# ---------------------------------------------------
# Prediction Section
# ---------------------------------------------------
if st.button("🚀 Predict"):
    try:
        # Create dataframe with correct feature names
        input_data = pd.DataFrame({
            "inflation": [inflation],
            "gdp": [gdp]
        })

        prediction = model.predict(input_data)

        st.success(f"📈 Predicted Value: {prediction[0]:.2f}")

        # Optional visualization
        st.subheader("📊 Prediction Visualization")
        chart_data = pd.DataFrame({
            "Value": [prediction[0]]
        })
        st.bar_chart(chart_data)

    except Exception as e:
        st.error("Something went wrong while making prediction.")
        st.write(e)

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("---")
st.caption("© 2026 Group 25 | Smart Inflation Project")
