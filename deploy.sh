#!/bin/bash

# Démarrer les services Docker Compose
docker-compose up -d --build

# Pousser l'image Docker vers Heroku
heroku container:push web -a petbook-back 

# Publier la nouvelle version de l'image Docker sur Heroku
heroku container:release web -a petbook-back

# Redémarrer les instances Heroku
heroku ps:restart -a petbook-back

