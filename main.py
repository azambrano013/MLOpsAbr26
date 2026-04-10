import numpy as np
import pandas as pd
import pickle
from fastapi import FastAPI
from pydantic import BaseModel, Field  # Importación vital

# 1. Definimos el esquema de datos
class Cliente(BaseModel):
    Income: float = Field(..., example=45000, description="Ingresos anuales del cliente en USD")
    IsFemale: int = Field(..., example=1, description="Género: 1 para Mujer, 0 para Hombre")
    IsRetired: int = Field(..., example=0, description="Estado de jubilación: 1 si está jubilado")
    Minors: int = Field(..., example=2, description="Número de hijos menores de edad")
    Own: int = Field(..., example=1, description="Propiedad de vivienda: 1 si es propietario")
    PrevChild: int = Field(..., example=1, description="Tiene hijos: 1 si es afirmativo")
    White: int = Field(..., example=0, description="Raza: 1 si es blanco")
# 2. Inicializamos FastAPI
app = FastAPI(
    title="🚀 API de Predicción - Niños Creativos",
    description="""
    Esta API utiliza un modelo de **Regresión Logística (ElasticNet)** para identificar clientes potenciales con alta probabilidad de suscripción a la nueva revista NINOS CREATIVOS de revistas de NoExisto.com.
    
    ### Autores:
    * **Lorena Anavia**
    * **Alberto Zambrano**
    """,
    version="1.0.0",
    contact={
        "name": "Equipo de Data Science - MLOPsAbr26 - NoExisto",
        "url": "http://noexisto.com/soporte",
        "email": "albertojosezambrano@gmail.com",
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
