#!/bin/bash

# Pousser l'image Docker vers Heroku
heroku container:push web 

# Publier la nouvelle version de l'image Docker sur Heroku
heroku container:release web 
