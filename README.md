Coffee Quality Prediction API ☕
This repository contains a containerized FastAPI application that serves a machine learning model to classify coffee quality into three categories: High, Average, and Low.

The project demonstrates a full MLOps pipeline—from training a Random Forest model on the Coffee Quality Institute (CQI) dataset to deploying it as a secure REST API on the cloud using Docker and Render.

🚀 Live API Endpoint
The API is live and can be accessed at:
URL: https://coffee-quality-api.onrender.com/docs

(Note: Use the /docs suffix to access the interactive Swagger UI).

🛠 Tech Stack
Language: Python 3.12

Model: Random Forest Classifier (Scikit-Learn)

API Framework: FastAPI

Containerization: Docker

Cloud Hosting: Render (Cloud-agnostic Docker architecture)

Environment: Google Colab (Training) & VS Code (Development)

📁 Repository Structure
main.py: The FastAPI application logic and API key security.

coffee_model.joblib: The pre-trained Random Forest model and preprocessing pipeline.

Dockerfile: Instructions for building the container image.

requirements.txt: List of dependencies with pinned versions (e.g., scikit-learn==1.6.0).

notebooks/: Contains the Google Colab notebook used for EDA and training.

🔒 Security
The /predict endpoint is secured with API Key Authentication. To make a successful request, you must include the following in your request header:

Header Key: x-api-key

Header Value: coffee_secret_123

💻 Local Setup (Docker)
To run this project locally, ensure you have Docker installed and follow these steps:

Clone the repository:

Bash
git clone https://github.com/areyousatisfy23-ui/coffee-quality-api.git
cd coffee-quality-api
Build the Docker image:

Bash
docker build -t coffee-api .
Run the container:

Bash
docker run -p 8000:8000 coffee-api
Access the API:
Open your browser and navigate to http://localhost:8000/docs.

📊 Sample Input Data
To test the prediction, you can use the following JSON payload:

JSON
{
  "Country_of_Origin": "Ethiopia",
  "Altitude": 1950.0,
  "Variety": "Arusha",
  "Processing_Method": "Washed / Wet",
  "Color": "Green",
  "Moisture_Percentage": 0.12
}
🏗 Deployment Architecture
The deployment follows a CI/CD workflow:

Push code to GitHub.

Render detects the change and triggers a build using the Dockerfile.

Docker installs the environment and pins scikit-learn to prevent version mismatches.

The container is deployed to a live URL.
