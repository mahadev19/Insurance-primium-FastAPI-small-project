# Import BaseModel from Pydantic
# BaseModel is used to define the structure of request/response data in FastAPI
from pydantic import BaseModel, Field

# Import Dict type for defining dictionary data types
from typing import Dict


# ---------------------------------------------------------
# RESPONSE SCHEMA
# This defines the structure of the response returned by the API
# FastAPI will automatically validate and document this
# ---------------------------------------------------------

class PredictionResponse(BaseModel):

    # Predicted insurance premium category
    # Example: Low / Medium / High
    predicted_category: str = Field(
        ...,  # "..." means this field is required
        description='The predicted insurance premium category',
        example='High'
    )

    # Confidence score of the predicted class
    # Value will be between 0 and 1
    confidence: float = Field(
        ...,  # required field
        description='Model confidence score for the predicted class (range: 0 to 1)',
        example=0.8432
    )

    # Dictionary containing probability for each class
    # Example: {'Low': 0.01, 'Medium': 0.15, 'High': 0.84}
    class_probabilities: Dict[str, float] = Field(
        ...,  # required field
        description='Probability distribution across all possible classes',
        example={'Low': 0.01, 'Medium': 0.15, 'High': 0.84}
    )