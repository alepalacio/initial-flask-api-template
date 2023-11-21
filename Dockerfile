# Utiliza una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto en el que se ejecuta la aplicación
EXPOSE 8000

# Ejecuta la aplicación con Gunicorn
CMD ["gunicorn", "-w", "4","--bind", "0.0.0.0:8000", "main:app", "--log-level=info", "--log-file=-"]