# myscript.py

import os

import django

from Login.models import Utilisateur

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mon_projet.settings')
django.setup()

# Ajoutez vos données ici
donnees_initiales = [
    {'email': 'charraimajdoline@gmail.com', 'Mot de passe': 'Maj-098765'},
    {'email': 'charraimanal@gmail.com', 'Mot de passe': 'Fadwa-0987'},
    # Ajoutez d'autres données au besoin
]

for donnee in donnees_initiales:
    objet = Utilisateur(**donnee)
    objet.save()
