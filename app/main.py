from fastapi import FastAPI, Header, HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel

# 1. Initialize FastAPI
app = FastAPI()

# 2. Load the "Cleaner" and the "Brain" at startup
model = joblib.load("app/model.joblib")
preprocessor = joblib.load("app/preprocessor.joblib")

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
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    input_df = pd.DataFrame([data.dict()])
    input_df.columns = ['Country of Origin', 'Altitude', 'Variety', 'Processing Method', 'Color', 'Moisture Percentage']
    
    processed_data = preprocessor.transform(input_df)
    prediction = model.predict(processed_data)
    
    result = "High Quality" if prediction[0] == 1 else "Average Quality"
    return {"prediction": result}