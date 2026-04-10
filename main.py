import numpy as np
import pandas as pd
import pickle
from fastapi import FastAPI
from pydantic import BaseModel  # Importación vital

# 1. Definimos el esquema de datos
class Cliente(BaseModel):
    Income: float
    IsFemale: int
    IsRetired: int
    Minors: int
    Own: int
    PrevChild: int
    White: int

# 2. Inicializamos FastAPI
app = FastAPI(
    title="🚀 API de Predicción - Niños Creativos",
    description="""
    Esta API utiliza un modelo de **Regresión Logística (ElasticNet)** para identificar clientes potenciales con alta probabilidad de suscripción a revistas de NoExisto.com.
    
    ### Autores:
    * **Lorena Anavia**
    * **Alberto Zambrano**
    """,
    version="1.0.0",
    contact={
        "name": "Equipo de Data Science - MLOPsAbr26 - NoExisto",
        "url": "http://noexisto.com/soporte",
        "email": "alberto@ejemplo.com",
    },
)

# 3. Cargamos el modelo (Asegúrate de que el nombre del archivo sea el correcto)
try:
    with open('modelo.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)
    print("✅ Modelo cargado exitosamente.")
except Exception as e:
    print(f"❌ Error crítico al cargar el modelo: {e}")
    modelo = None

# 4. Endpoint de predicción
@app.post("/predict")
def hacer_prediccion(datos: Cliente):
    if modelo is None:
        return {"error": "El servidor no tiene un modelo cargado."}
    
    # Convertimos a DataFrame (usamos model_dump para Pydantic V2)
    datos_df = pd.DataFrame([datos.model_dump()])
    
    # Realizamos la predicción
    resultado = modelo.predict(datos_df)
    
    return {"prediccion": int(resultado[0])}
