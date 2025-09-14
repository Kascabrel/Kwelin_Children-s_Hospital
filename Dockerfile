# ======================
#   DOCKERFILE
# ======================

# Étape 1 : base image
FROM python:3.11-slim

# Étape 2 : define the work derictory
WORKDIR /app

# Étape 3 : install system dépendancies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Étape 4 : copy requirements
COPY requirements.txt .

# Étape 5 : install Python dependancies
RUN pip install --no-cache-dir -r requirements.txt

# Étape 6 : copier files
COPY run.py .
COPY app ./app
COPY requirements.txt .


# Étape 7 : environnement variables
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Étape 8 : expose the port
EXPOSE 5000

# Étape 9 : Start/run with Gunicorn (more robuster than flask run)
# -b : bind host:port
# "run:app" → correspond à run.py qui contient app = create_app()
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
