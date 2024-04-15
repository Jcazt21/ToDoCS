# Usa la imagen base de Python 3.8
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el código fuente de la aplicación y el archivo requirements.txt
COPY . .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar la aplicación cuando el contenedor se inicia
CMD ["python", "main.py"]
