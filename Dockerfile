# ======================
#   DOCKERFILE
# ======================

# Étape 1 : base image
FROM python:3.11-slim

# Étape 2 : définir répertoire de travail
WORKDIR /app

# Étape 3 : installer dépendances système utiles
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Étape 4 : copier requirements
COPY requirements.txt .

# Étape 5 : installer dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Étape 6 : copier uniquement ce qui est utile
COPY run.py .
COPY app ./app
COPY requirements.txt .


# Étape 7 : variables d’environnement
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Étape 8 : exposer le port
EXPOSE 5000

# Étape 9 : lancer avec Gunicorn (plus robuste que flask run)
# -b : bind host:port
# "run:app" → correspond à run.py qui contient app = create_app()
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
