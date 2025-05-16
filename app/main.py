#imports
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os

#define the input data schema with pydantic
class InputData(BaseModel):
    MedInc: float
    AveRooms: float
    AveOccup: float

#initialize FastAPI app

app = FastAPI(title='House Price Prediction API')

#load the model during startup
model_path = os.path.join("model","linear_regression_model.pkl")
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(data: InputData):
    # Prepare the data for prediction
    input_features = [[data.MedInc, data.AveRooms, data.AveOccup]]

    #make prediction
    prediction = model.predict(input_features)

    #return the prediction 
    return {"Predicted_house_price": prediction[0]}


"""
This FastAPI application exposes a /predict endpoint 
that takes three features (MedInc, AveRooms, AveOccup). 
It uses the trained model to predict house prices, 
and returns the predicted price.
"""