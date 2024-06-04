# Votre fichier où vous utilisez la fonction create_test_user()
import logging
from .models import RHUser

#logger = logging.getLogger(__name__)
def create_test_user():
    email = "test@example.com"
    password = "motdepasse123"
    user = RHUser.objects.create(email=email, password=password)
    #logger.debug("Utilisateur créé avec succès : %s", user)
    return user
