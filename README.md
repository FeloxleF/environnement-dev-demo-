# Environnement de développement application web 

environnment de développement pour une application WEB avec des conteneurs docker, réalisé dans le cadre d'une présentation académique.
L'environnement compprends les outils suivants :  

BACK : FastAPI - python  
FRONT : Angular - typescript/javascript  
BDD : MariaDB (similaire à mysql)  


## Installer l'environnment 

### windows  

installer docker desktop et docker compose (inclus das docker desktop)  
--> https://www.docker.com/products/docker-desktop/  

### mac et linux  
voir la procedure indiquée : https://www.docker.com/products/docker-desktop/

### utilisation des conteneurs  

récuperer le dépot github sur votre machine  
démarrer le docker engine --> ouvrir docker desktop sur votre machine  
ouvrir un terminal à la racine du dossier  
  
tapez ```docker-compose up``` pour crééer et démarrer les conteneurs  
tapez ```docker-compose stop``` pour arrêter les containeurs (sans les supprimer)  
tapez ````docker-compose start```` pour démarrer les containeurs (si ils existent)  
tapez ```docker-compose down``` pour supprimer les conteneurs

## utiliser l'environnment

le back et la bdd sont déjà reliés entre eux  
la bdd est déjà initialisée avec le fichier ````init.sql```` qui se trouve dans le sous dossier database  

le serveur python (backend) est accessible sur le port 8000 --> ````http://localhost:8000/````  
le serveur angular (frontend) est accessible sur le port 4200 --> ````http://localhost:4200/````  

l'url ````http://localhost:8000/phrases```` renvoie les phrases (et leur id) rentrées dans la bdd

