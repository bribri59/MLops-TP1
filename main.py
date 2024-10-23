from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Charger le modèle
model = joblib.load("regression.joblib")

# Créer l'API FastAPI
app = FastAPI()

# Schéma pour les données d'entrée
class HouseInfo(BaseModel):
    size: float
    bedrooms: int
    garden: int

# Endpoint de prédiction
@app.post("/predict")
def predict_price(info: HouseInfo):
    input_data = [[info.size, info.bedrooms, info.garden]]
    prediction = model.predict(input_data)
    return {"prediction": prediction[0]}
