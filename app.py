import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.sidebar.header("About this App")
st.sidebar.info(
    """
    This app predicts inflation impact based on user inputs.
    
    Developed by **Group 25**.
    """
)

st.set_page_config(page_title="Smart Inflation Forecasting System", layout="centered")

st.title("📊 Smart Inflation Prediction System")
st.markdown("Welcome to our **Smart Inflation Analysis App**. Enter your data below to see predictions!")


st.write("---")

st.subheader("Enter Economic Indicators")

gdp_growth = st.number_input("GDP Growth Rate (%)", min_value=-10.0, max_value=20.0, value=5.0)
interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=30.0, value=10.0)
exchange_rate = st.number_input("Exchange Rate (TZS per USD)", min_value=1000.0, max_value=5000.0, value=2500.0)
unemployment = st.number_input("Unemployment Rate (%)", min_value=0.0, max_value=50.0, value=10.0)
money_supply = st.number_input("Money Supply (M2)", min_value=0.0, value=1000.0)


st.write("---")

if st.button("Predict Inflation Rate"):

    # Prepare input data
    input_data = np.array([[gdp_growth, interest_rate, exchange_rate, unemployment,money_supply]])

     # Make prediction
    prediction = model.predict(input_data)

    # Display result
    st.success(f"Predicted Inflation Rate: {prediction[0]:.2f}%")

    # Interpretation
    if prediction[0] < 5:
        st.info("Inflation is considered LOW and stable.")
    elif prediction[0] < 10:
        st.warning("Inflation is MODERATE.")
    else:
        st.error("Inflation is HIGH. Economic pressure may increase.")









