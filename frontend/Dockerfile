# Étape de build
FROM node:20-alpine AS angular


# Définir le répertoire de travail dans le conteneur
WORKDIR /code

# Copier les fichiers package.json et package-lock.json dans le conteneur
COPY . .
# Installer Angular CLI
RUN npm install -g @angular/cli
RUN npm install



EXPOSE 4200
# CMD ng serve --host 0.0.0.0 --port 4200 --open

CMD npm start




