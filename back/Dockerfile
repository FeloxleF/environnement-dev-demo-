# Utilise l'image Python officielle comme base
FROM python:3.10

# Définit le répertoire de travail dans le conteneur
WORKDIR /code

COPY ./requirement.txt ./

# Installe les dépendances FastAPI et Uvicorn
RUN pip install --no-cache-dir -r requirement.txt

COPY ./src ./src

# Expose le port 8000 pour accéder à l'application FastAPI
EXPOSE 8000

# Commande pour démarrer l'application FastAPI avec Uvicorn
#CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]


