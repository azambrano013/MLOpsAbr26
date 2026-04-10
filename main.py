import numpy as np
import pandas as pd
import pickle
from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict

# 1. Definimos el esquema de datos con descripciones y ejemplos claros
class Cliente(BaseModel):
    Income: float = Field(..., description="Ingresos anuales del cliente en USD")
    IsFemale: int = Field(..., description="Género: 1 para Mujer, 0 para Hombre")
    IsRetired: int = Field(..., description="Estado de jubilación: 1 si está jubilado")
    Minors: int = Field(..., description="Número de hijos menores de edad")
    Own: int = Field(..., description="Propiedad de vivienda: 1 si es propietario")
    PrevChild: int = Field(..., description="Tiene hijos: 1 si es afirmativo")
    White: int = Field(..., description="Raza: 1 si es blanco")

    # Esta configuración permite que el "Example Value" se llene automáticamente en la UI
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "Income": 45000.0,
                    "IsFemale": 1,
                    "IsRetired": 0,
                    "Minors": 2,
                    "Own": 1,
                    "PrevChild": 1,
                    "White": 0
                }
            ]
        }
    )

# 2. Inicializamos FastAPI con metadatos extendidos
app = FastAPI(
    title="🚀 API de Predicción: Revista Niños Creativos-LAnavia-AZambrano",
    description="""
    ## Propósito
    Esta API utiliza un modelo de **Regresión Logística con regularización ElasticNet** para predecir la propensión de suscripción de clientes potenciales para la editorial **NoExisto.com**.

    ## Instrucciones
    1. Haz clic en el botón **POST /predict**.
    2. Presiona **Try it out**.
    3. Ajusta los valores en el JSON de entrada.
    4. Revisa la sección **Response body** para ver el resultado (1: Suscribe, 0: No suscribe).

    ### Equipo de Desarrollo - 19 Abril 2026:
    * **Lorena Anavia**
    * **Alberto Zambrano**
    """,
    version="1.1.0",
    contact={
        "name": "Soporte Técnico - Data Science Team",
        "url": "http://noexisto.com/soporte",
        "email": "albertojosezambrano@gmail.com",
    },
)

# 3. Carga segura del modelo
try:
    with open('modelo.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)
    print("✅ Modelo cargado exitosamente.")
except Exception as e:
    print(f"❌ Error crítico al cargar el modelo: {e}")
    modelo = None

# 4. Endpoint de predicción organizado por etiquetas (Tags)
@app.post("/predict", tags=["Servicios de Inferencia"])
def hacer_prediccion(datos: Cliente):
    """
    Recibe los datos demográficos del cliente y devuelve la predicción de suscripción.
    """
    if modelo is None:
        return {"error": "El servidor no tiene un modelo cargado."}
    
    # Convertimos los datos de entrada a DataFrame
    datos_df = pd.DataFrame([datos.model_dump()])
    
    # Realizamos la predicción
    resultado = modelo.predict(datos_df)
    
    return {
        "prediccion": int(resultado[0]),
        "mensaje": "El cliente es propenso a suscribirse" if resultado[0] == 1 else "El cliente no es propenso a suscribirse"
    }
