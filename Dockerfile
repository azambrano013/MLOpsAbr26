# 1. Usamos una imagen de Python ligera como base
FROM python:3.12

# 2. Creamos una carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos el archivo de requisitos primero (para optimizar la cache)
COPY requirements.txt .

# 4. Instalamos las librerías directamente en el contenedor
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos todo el resto del código (incluyendo tu modelo.pkl)
COPY . .

# 6. Comando para arrancar la API cuando el contenedor se encienda desde Heroku
CMD uvicorn main:app --host 0.0.0.0 --port $PORT