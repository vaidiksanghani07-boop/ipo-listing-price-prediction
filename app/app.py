import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


model_path = Path(__file__).parent.parent / "notebooks" / "best_random_forest_model.pkl"
model = joblib.load(model_path)


st.title("IPO Listing Price Prediction")

st.write("Enter IPO details to predict the expected listing price.")

st.header("Enter Information")

issue_size = st.number_input("Issue Size (₹ Crores)",min_value=0.0,value=100.0,step=0.01)

qib = st.number_input("QIB Subscription (x)",min_value=0.0,value=1.0,step=0.01)

hni = st.number_input("HNI Subscription (x)",min_value=0.0,value=1.0,step=0.01)

rii = st.number_input("Reatil Subscription (x)",min_value=0.0,value=1.0,step=0.01)

total = st.number_input("Total Subscription (x)",min_value=0.0,value=1.0,step=0.01)

offer_price = st.number_input("Offer Price (₹)",min_value=0.0,value=100.0,step=0.01)


if st.button("Predict Listing Price"):

    input_data = pd.DataFrame({
        "Issue_Size(crores)": [issue_size],
        "QIB": [qib],
        "HNI": [hni],
        "RII": [rii],
        "Total": [total],
        "Offer Price": [offer_price]
    })

    prediction = model.predict(input_data)

    predicted_price = prediction[0]

    st.success(
        f"Predicted Listing Price: ₹{predicted_price:.2f}"
    )