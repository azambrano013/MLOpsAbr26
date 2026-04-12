import numpy as np
import pandas as pd
import pickle
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ConfigDict

# Orden de columnas exacto con el que fue entrenado el pipeline
FEATURES = ['Income', 'IsFemale', 'IsRetired', 'Minors', 'Own', 'PrevChild', 'White']

class Cliente(BaseModel):
    Income: float = Field(..., description="Ingresos anuales del cliente en USD")
    IsFemale: int = Field(..., description="Género: 1 para Mujer, 0 para Hombre")
    IsRetired: int = Field(..., description="Estado de jubilación: 1 si está jubilado")
    Minors: int = Field(..., description="Número de hijos menores de edad")
    Own: int = Field(..., description="Propiedad de vivienda: 1 si es propietario")
    PrevChild: int = Field(..., description="Compró revistas infantiles antes: 1 si es afirmativo")
    White: int = Field(..., description="Raza: 1 si es blanco")

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

app = FastAPI(
    title="🚀 API de Predicción: Revista Niños Creativos-LAnavia-AZambrano",
    description="""
## Propósito
Esta API utiliza un modelo de **Regresión Logística con regularización ElasticNet** para predecir
la propensión de suscripción de clientes potenciales a la nueva revista NINOS CREATIVOS para la editorial **NoExisto.com**.

## Instrucciones
1. Haz clic en el botón **POST /predict**.
2. Presiona **Try it out**.
3. Ajusta los valores en el JSON de entrada. Según las siguientes instrucciones: 
    3.1.     Income:        Ingresos anuales del cliente en USD
    3.2.     IsFemale:      Género: 1 para Mujer, 0 para Hombre
    3.3.     IsRetired:     Estado de jubilación: 1 si está jubilado
    3.4.     Minors:        Número de hijos menores de edad
    3.5.     Own:           Propiedad de vivienda: 1 si es propietario
    3.6.     PrevChild:     Compró revistas infantiles antes: 1 si es afirmativo
    3.7.     White:         Raza: 1 si es blanco
4. Revisa la sección **Response body** para ver el resultado.

### Equipo de Desarrollo - 19 Abril 2026:
* **Lorena Anavia**
* **Alberto Zambrano**
""",
    version="1.2.0",
    contact={
        "name": "Soporte Técnico - Data Science Team",
        "url": "http://noexisto.com/soporte",
        "email": "albertojosezambrano@gmail.com",
    },
)

# Carga segura del modelo (pipeline con scaler incluido)
try:
    with open('modelo.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)
    print("✅ Modelo cargado exitosamente.")
except Exception as e:
    print(f"❌ Error crítico al cargar el modelo: {e}")
    modelo = None

@app.get("/health", tags=["Estado del Servicio"])
def health_check():
    return {
        "status": "ok",
        "model_loaded": modelo is not None,
        "version": "1.2.0"
    }

@app.post("/predict", tags=["Servicios de Inferencia"])
def hacer_prediccion(datos: Cliente):
    if modelo is None:
        raise HTTPException(status_code=503, detail="Modelo no disponible")

    # Forzar el orden exacto de columnas con el que fue entrenado el pipeline
    datos_df = pd.DataFrame([datos.model_dump()])[FEATURES]

    resultado = modelo.predict(datos_df)
    probabilidad = modelo.predict_proba(datos_df)[0]

    return {
        "prediccion": int(resultado[0]),
        "mensaje": "El cliente es propenso a suscribirse" if resultado[0] == 1 else "El cliente no es propenso a suscribirse",
        "probabilidad_compra": round(float(probabilidad[1]), 4),
        "probabilidad_no_compra": round(float(probabilidad[0]), 4)
    }
