# Import BaseModel and Field for defining API input schema
# computed_field is used to create derived features automatically
# field_validator is used to validate or clean incoming data
from pydantic import BaseModel, Field, computed_field, field_validator

# Import typing utilities
# Literal restricts values to specific options
# Annotated allows adding validation rules to fields
from typing import Literal, Annotated

# Import city tier lists used to determine city category
from config.city_tier import tier_1_cities, tier_2_cities


# ------------------------------------------------------
# USER INPUT SCHEMA
# This defines the structure of data expected from user
# FastAPI automatically validates incoming requests
# ------------------------------------------------------

class UserInput(BaseModel):

    # -------------------------------
    # BASIC USER INPUT FEATURES
    # -------------------------------

    # Age must be between 1 and 119
    age: Annotated[
        int,
        Field(..., gt=0, lt=120, description='Age of the User')
    ]

    # Weight must be greater than 0
    weight: Annotated[
        float,
        Field(..., gt=0, description='Weight of the User')
    ]

    # Height must be greater than 0
    height: Annotated[
        float,
        Field(..., gt=0, description='Height of the User')
    ]

    # Annual income in Lakhs Per Annum
    income_lpa: Annotated[
        float,
        Field(..., gt=0, description='Annual Salary of the User in LPA')
    ]

    # Whether the user smokes or not
    smoker: Annotated[
        bool,
        Field(..., description='Is user a smoker')
    ]

    # City name
    city: Annotated[
        str,
        Field(..., description='The city that user belongs to')
    ]

    # Occupation limited to specific categories
    occupation: Annotated[
        Literal[
            'retired',
            'freelancer',
            'student',
            'government_job',
            'business_owner',
            'unemployed',
            'private_job'
        ],
        Field(..., description='Occupation of the user')
    ]


    # --------------------------------------------------
    # FIELD VALIDATOR
    # Used to clean/normalize city input
    # --------------------------------------------------

    @field_validator('city')
    @classmethod
    def normalize_city(cls, v: str) -> str:

        # Remove extra spaces and convert to proper format
        # Example: " mumbai " -> "Mumbai"
        v = v.strip().title()

        return v


    # --------------------------------------------------
    # COMPUTED FIELD: BMI
    # BMI = weight / height²
    # This is automatically calculated from user input
    # --------------------------------------------------

    @computed_field
    @property
    def bmi(self) -> float:

        return self.weight / (self.height ** 2)


    # --------------------------------------------------
    # COMPUTED FIELD: LIFESTYLE RISK
    # Determines health risk based on smoking + BMI
    # --------------------------------------------------

    @computed_field
    @property
    def lifestyle_risk(self) -> str:

        if self.smoker and self.bmi > 30:
            return 'high'

        elif self.smoker and self.bmi > 27:
            return 'medium'

        else:
            return 'low'


    # --------------------------------------------------
    # COMPUTED FIELD: AGE GROUP
    # Converts numeric age into categorical group
    # --------------------------------------------------

    @computed_field
    @property
    def age_group(self) -> str:

        if self.age < 25:
            return 'Young'

        elif self.age < 45:
            return 'adult'

        elif self.age < 60:
            return "middle_aged"

        return 'Senior'


    # --------------------------------------------------
    # COMPUTED FIELD: CITY TIER
    # Converts city name into tier category
    # Tier 1 -> major metro cities
    # Tier 2 -> mid-size cities
    # Tier 3 -> smaller cities
    # --------------------------------------------------

    @computed_field
    @property
    def city_tier(self) -> int:

        if self.city in tier_1_cities:
            return 1

        elif self.city in tier_2_cities:
            return 2

        else:
            return 3