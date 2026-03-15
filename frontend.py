# Import Streamlit library for building the web interface
import streamlit as st

# Import requests library to send HTTP requests to FastAPI API
import requests


# URL of the FastAPI prediction endpoint
# This API will receive user data and return prediction
API_URL = "http://3.87.154.163:8000/predict" 


# Title of the Streamlit application
st.title("Insurance Premium Category Predictor")

# Short description for the user
st.markdown("Enter your details below:")


# -------------------------
# USER INPUT FIELDS
# These fields collect input from the user
# -------------------------

# Age input field
age = st.number_input(
    "Age",
    min_value=1,
    max_value=119,
    value=30
)

# Weight input field (in kilograms)
weight = st.number_input(
    "Weight (kg)",
    min_value=1.0,
    value=65.0
)

# Height input field (in meters)
height = st.number_input(
    "Height (m)",
    min_value=0.5,
    max_value=2.5,
    value=1.7
)

# Annual income input (Lakhs Per Annum)
income_lpa = st.number_input(
    "Annual Income (LPA)",
    min_value=0.1,
    value=10.0
)

# Dropdown to choose smoker status
smoker = st.selectbox(
    "Are you a smoker?",
    options=[True, False]
)

# Text input field for city name
city = st.text_input(
    "City",
    value="Mumbai"
)

# Dropdown for selecting occupation
occupation = st.selectbox(
    "Occupation",
    [
        'retired',
        'freelancer',
        'student',
        'government_job',
        'business_owner',
        'unemployed',
        'private_job'
    ]
)


# ---------------------------------------------------
# PREDICTION BUTTON
# When user clicks this button, API request is sent
# ---------------------------------------------------
if st.button("Predict Premium Category"):

    # Create dictionary of user inputs
    # This data will be sent to the FastAPI backend
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:

        # Send POST request to FastAPI API with user data
        response = requests.post(API_URL, json=input_data)

        # Convert API response to Python dictionary
        result = response.json()

        # Check if request was successful
        if response.status_code == 200 and "response" in result:

            # Extract prediction data
            prediction = result["response"]

            # Show predicted premium category
            st.success(
                f"Predicted Insurance Premium Category: **{prediction['predicted_category']}**"
            )

            # Show model confidence
            st.write("🔍 Confidence:", prediction["confidence"])

            # Show probability of each class
            st.write("📊 Class Probabilities:")

            # Display probabilities in JSON format
            st.json(prediction["class_probabilities"])

        else:
            # Show API error if something went wrong
            st.error(f"API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:

        # Show error if Streamlit cannot connect to FastAPI server
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")