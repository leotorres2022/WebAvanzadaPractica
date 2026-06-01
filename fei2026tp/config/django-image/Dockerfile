FROM python:3.12.2-bookworm

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Actualizar el sistema e instalar dependencias básicas si hiciera falta
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el script de entrada y darle permisos de ejecución
COPY arranque.sh /usr/local/bin/arranque.sh
RUN sed -i 's/\r$//' /usr/local/bin/arranque.sh && chmod +x /usr/local/bin/arranque.sh


# El contenedor trabajará montando la carpeta backend sobre /app
CMD ["/bin/bash", "/usr/local/bin/arranque.sh"]