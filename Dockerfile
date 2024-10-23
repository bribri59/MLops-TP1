# Utiliser une image Python de base
FROM python:3.9-slim

# Installer les dépendances
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier l'application
COPY . .

# Exposer le port
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
