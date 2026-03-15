# Import FastAPI framework
from fastapi import FastAPI

# JSONResponse allows us to send custom JSON responses with status codes
from fastapi.responses import JSONResponse

# Import the ML prediction function and model details
# predict_output -> function that takes input data and returns prediction
# model -> the trained ML model
# MODEL_VERSION -> version of the model (useful in production)
from model.predict import predict_output, model, MODEL_VERSSION

# Import input schema (defines what data user must send)
from schema.user_input import UserInput

# Import response schema (defines how API response should look)
from schema.prediction_response import PredictionResponse


# Create FastAPI application instance
app = FastAPI()


# -----------------------------------------------------------
# ROOT ENDPOINT
# This is a simple endpoint for humans to check if API is running
# Example: http://127.0.0.1:8000/
# -----------------------------------------------------------
@app.get("/")
def home():
    return {
        "message": "Insurance Premium Prediction API is running"
    }


# -----------------------------------------------------------
# HEALTH CHECK ENDPOINT
# Used by machines/monitoring tools to check API health
# Example: http://127.0.0.1:8000/health
# -----------------------------------------------------------
@app.get('/health')
def health_check():
    return {
        "status": "ok",                 # API working properly
        "Version": "1.0.0",             # API version
        "model_loaded": model is not None  # Checks if ML model loaded successfully
    }


# -----------------------------------------------------------
# PREDICTION ENDPOINT
# This endpoint receives user data and returns predicted
# insurance premium category
# -----------------------------------------------------------
@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):

    # Convert input object into dictionary
    # This format is expected by the ML prediction function
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:

        # Call prediction function from model
        prediction = predict_output(user_input)

        # Return prediction as JSON response
        return JSONResponse(
            status_code=200,
            content={'response': prediction}
        )

    except Exception as e:

        # If something goes wrong, return error message
        return JSONResponse(
            status_code=500,
            content=str(e)
        )# Import FastAPI framework
from fastapi import FastAPI

# JSONResponse allows us to send custom JSON responses with status codes
from fastapi.responses import JSONResponse

# Import the ML prediction function and model details
# predict_output -> function that takes input data and returns prediction
# model -> the trained ML model
# MODEL_VERSION -> version of the model (useful in production)
from model.predict import predict_output, model, MODEL_VERSSION

# Import input schema (defines what data user must send)
from schema.user_input import UserInput

# Import response schema (defines how API response should look)
from schema.prediction_response import PredictionResponse


# Create FastAPI application instance
app = FastAPI()


# -----------------------------------------------------------
# ROOT ENDPOINT
# This is a simple endpoint for humans to check if API is running
# Example: http://127.0.0.1:8000/
# -----------------------------------------------------------
@app.get("/")
def home():
    return {
        "message": "Insurance Premium Prediction API is running"
    }


# -----------------------------------------------------------
# HEALTH CHECK ENDPOINT
# Used by machines/monitoring tools to check API health
# Example: http://127.0.0.1:8000/health
# -----------------------------------------------------------
@app.get('/health')
def health_check():
    return {
        "status": "ok",                 # API working properly
        "Version": "1.0.0",             # API version
        "model_loaded": model is not None  # Checks if ML model loaded successfully
    }


# -----------------------------------------------------------
# PREDICTION ENDPOINT
# This endpoint receives user data and returns predicted
# insurance premium category
# -----------------------------------------------------------
@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):

    # Convert input object into dictionary
    # This format is expected by the ML prediction function
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:

        # Call prediction function from model
        prediction = predict_output(user_input)

        # Return prediction as JSON response
        return JSONResponse(
            status_code=200,
            content={'response': prediction}
        )

    except Exception as e:

        # If something goes wrong, return error message
        return JSONResponse(
            status_code=500,
            content=str(e)
        )