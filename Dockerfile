# Use official lightweight Python 3.11 image as base
# "slim" version keeps the image small
FROM python:3.11-slim 


# Set working directory inside the container
# All commands will run from this folder
WORKDIR /APP


# Copy requirements.txt file from local machine to container
# This file contains all Python dependencies needed for the project
COPY requirements.txt .


# Install all required Python packages
# --no-cache-dir prevents pip from storing cache to keep image size small
RUN pip install --no-cache-dir -r requirements.txt


# Copy the entire project code from local machine to container
COPY . .


# Expose port 8000 so the container can accept external requests
# FastAPI (uvicorn) will run on this port
EXPOSE 8000


# Command to start the FastAPI application
# uvicorn runs the app and makes it accessible on the network
# app:app means
#   first "app" = file name (app.py)
#   second "app" = FastAPI instance inside that file
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]