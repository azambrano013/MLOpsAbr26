# 🎨 API Niños Creativos - NoExisto.com

Esta API proporciona un servicio de predicción basado en un modelo de **Regresión Logística** para optimizar las campañas de marketing de suscripción a revistas para Niños.

## 📝 Descripción del Problema
El objetivo de este proyecto es ayudar a la empresa **NoExisto.com** a identificar qué clientes potenciales tienen una mayor probabilidad de suscribirse a una revista nueva llamada NINOS CREATIVOS.  

Utilizando datos demográficos y de comportamiento, el modelo de Aprendizaje Supervisado (ElasticNet Logistic Regression) analiza variables como el nivel de ingresos, género, etnia y estado de jubilación para clasificar a los usuarios. Esto permite una estrategia de marketing más inteligente, reduciendo costos de captación y mejorando la relevancia de las ofertas enviadas a los clientes.

---

## 🚀 Instrucciones para correr la API localmente

Sigue estos pasos para configurar el entorno y ejecutar el servidor en tu computadora:

1. **Clonar el repositorio o situarse en la carpeta:**
   ```bash
   cd api-ninos-creativos
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   # Crear la burbuja (entorno virtual)
   python -m venv venv

   # Activar en Windows
   .\venv\Scripts\activate
   ```

3. **Instalar las dependencias:**
   Asegúrate de tener el archivo `requirements.txt` y ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

4. **Iniciar el servidor con Uvicorn:**
   ```bash
   uvicorn main:app --reload
   ```
   El servidor estará disponible en: `http://127.0.0.1:8000`

5. **Importante tener el archivo runtime.txt que estipula que la versión de Python debe ser 3.10 o superior**

---

## 🛠 Ejemplo de Request al endpoint `/predict`

Puedes probar la API directamente desde `http://127.0.0.1:8000/docs` o usando una herramienta como Postman o cURL.

**Cuerpo del JSON (Ejemplo):**
```json
{
  "Income": 45000,
  "IsFemale": 1,
  "IsRetired": 0,
  "HasChildren": 1,
  "Age": 34
}
```

**Respuesta esperada:**
```json
{
  "prediction": 1,
  "probability": 0.85,
  "message": "El cliente es propenso a suscribirse"
}
```

---

## ☁️ Plataforma Cloud usada para el deploy

Para este proyecto se ha seleccionado la plataforma **Render** (o Hugging Face/Railway, según la que hayas elegido finalmente), debido a su facilidad para desplegar aplicaciones de Python y FastAPI mediante contenedores o integración directa con GitHub.

---

### 💡 Notas adicionales
* El modelo fue entrenado usando `scikit-learn`.
* El archivo del modelo está guardado como `modelo.pkl`.
* Se utiliza `FastAPI` por su alto rendimiento y generación automática de documentación interactiva.

---

## 💻 Instalación y Configuración (Pasos de la Rúbrica)

Sigue estos pasos para replicar el entorno en tu máquina local:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/azambrano013/MLOpsAbr26.git](https://github.com/azambrano013/MLOpsAbr26.git)
cd api-ninos-creativos
