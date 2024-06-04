# populate_conges.py

import os
import django

# Configuration de l'environnement Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GRH.settings')
django.setup()

from Home.models import Conge

def populate_conges():
    # Créer des instances de modèle Conge
    Conge.objects.create(employe="manal", date_debut="2024-04-10", date_fin="2024-04-12", reason="Vacances annuelles")
    Conge.objects.create(employe="zou", date_debut="2024-05-05", date_fin="2024-05-10", reason="Congé de maladie")
    # Ajoutez d'autres instances de modèle Conge selon vos besoins

if __name__ == '__main__':
    populate_conges()
