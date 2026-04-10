🎨 API Niños Creativos - NoExisto.com
Esta API proporciona un servicio de predicción basado en un modelo de Regresión Logística (ElasticNet) para optimizar las campañas de marketing de suscripción a revistas.

🌐 Acceso Directo (Live Demo)
La API se encuentra desplegada y operativa en la nube. Puedes probarla sin instalar nada aquí:

👉 (https://mlopsabr26-1.onrender.com/docs)

📝 Descripción del Problema
El objetivo es identificar clientes potenciales con alta probabilidad de suscribirse a la nueva revista Niños Creativos. El modelo analiza variables demográficas (Ingresos, Edad, Hijos, etc.) para clasificar a los usuarios, permitiendo una estrategia de marketing más eficiente y con menores costos de captación para NoExisto.com.



---

🚀 Instrucciones para Ejecución Local
Si deseas correr el proyecto en tu propia máquina, tienes dos opciones:

Opción A: Con Docker (Recomendado) 🐳
Tener Docker Desktop abierto.

Construir la imagen:
docker build -t api-ninos-creativos .

Correr el contenedor:
docker run -p 8000:8000 api-ninos-creativos

Acceder a http://localhost:8000/docs.

Opción B: Con Entorno Virtual (Python)
Activar entorno virtual: .\venv\Scripts\activate

Instalar dependencias: pip install -r requirements.txt

Ejecutar: uvicorn main:app --reload

🛠 Estructura del Request (/predict)
Para obtener una predicción, envía un JSON con el siguiente formato:

JSON
{
  "Income": 45000,
  "IsFemale": 1,
  "IsRetired": 0,
  "Minors": 2,
  "Own": 1,
  "PrevChild": 1,
  "White": 0
}
☁️ Infraestructura
Plataforma Cloud: Render.

Despliegue: Automático mediante Dockerfile sincronizado con GitHub.

Framework: FastAPI.

Modelo: Scikit-learn (ElasticNet Logistic Regression).integración directa con GitHub.

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
