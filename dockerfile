# Utiliza una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar la aplicación
CMD ["python", "todo.py"]
