
    from fastapi import FastAPI, Header, HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel

# 1. Initialize FastAPI
app = FastAPI()

# 2. Load the model (Matching your exact GitHub filename)
# We assume the preprocessor is built into this joblib file
model = joblib.load("app/coffee_model.joblib")

# 3. Define the input format
class CoffeeInput(BaseModel):
    Country_of_Origin: str
    Altitude: float
    Variety: str
    Processing_Method: str
    Color: str
    Moisture_Percentage: float

# 4. Security: Simple API Key check
API_KEY = "coffee_secret_123"

@app.get("/")
def home():
    return {"message": "Coffee Quality API is Live!"}

@app.post("/predict")
def predict(data: CoffeeInput, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    # Matching column names to your training data
    input_df.columns = ['Country of Origin', 'Altitude', 'Variety', 'Processing Method', 'Color', 'Moisture Percentage']
    
    prediction = model.predict(input_df)
    
    # Mapping to our 3 classes: Low, Average, High
    quality_map = {0: "Low Quality", 1: "Average Quality", 2: "High Quality"}
    result = quality_map.get(prediction[0], "Unknown Quality")
    
    return {"prediction": result}
