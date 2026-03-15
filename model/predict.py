# Import pickle library
# Pickle is used to load the trained machine learning model saved as a file
import pickle

# Import pandas for creating DataFrame from input data
import pandas as pd


# -------------------------------------------------
# LOAD TRAINED MACHINE LEARNING MODEL
# -------------------------------------------------

# Open the saved model file (model.pkl) in read-binary mode
with open('model/model.pkl', 'rb') as f:

    # Load the model into memory
    model = pickle.load(f)


# -------------------------------------------------
# MODEL VERSION (useful for tracking model updates)
# -------------------------------------------------

# Version of the ML model (useful in production systems)
MODEL_VERSSION = '1.0.0'


# -------------------------------------------------
# GET CLASS LABELS FROM THE MODEL
# -------------------------------------------------

# model.classes_ gives all possible target classes used during training
# Example: ['Low', 'Medium', 'High']

# Convert them into a Python list
class_labels = model.classes_.tolist()


# -------------------------------------------------
# PREDICTION FUNCTION
# This function will be called by the FastAPI endpoint
# -------------------------------------------------

def predict_output(user_input: dict):

    # Convert user input dictionary into a pandas DataFrame
    # Model expects input in tabular format
    df = pd.DataFrame([user_input])

    
    # -------------------------------
    # PREDICT THE CLASS
    # -------------------------------

    # Predict the insurance premium category
    predicted_class = model.predict(df)[0]


    # -------------------------------
    # GET PROBABILITIES
    # -------------------------------

    # predict_proba returns probability for each class
    # Example: [0.1, 0.7, 0.2]
    probabilities = model.predict_proba(df)[0]

    # Highest probability is considered model confidence
    confidence = max(probabilities)


    # -------------------------------
    # CREATE CLASS-PROBABILITY MAPPING
    # -------------------------------

    # Combine class labels with their probabilities
    # Example: {'Low':0.1,'Medium':0.7,'High':0.2}
    class_probs = dict(
        zip(
            class_labels,
            map(lambda p: round(p, 4), probabilities)  # round probabilities to 4 decimal places
        )
    )


    # -------------------------------
    # RETURN FINAL RESPONSE
    # -------------------------------

    # This dictionary will be returned to FastAPI
    # and then sent back to the frontend (Streamlit)
    return {
        'predicted_category': predicted_class,   # predicted insurance premium category
        'confidence': round(confidence, 4),      # model confidence score
        'class_probabilities': class_probs       # probability for each class
    }