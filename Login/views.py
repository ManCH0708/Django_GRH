# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import RHUser
from .utils import create_test_user
from django.http import HttpRequest

from django.shortcuts import redirect


def my_view(request):
    new_user = create_test_user()
    if new_user:
        messages.success(request, "Utilisateur de test créé avec succès.")
    else:
        messages.error(request, "Erreur lors de la création de l'utilisateur de test.")

    return redirect('home')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = RHUser.objects.get(email=email)
            if check_password(password, user.password):
                # Authentification réussie, rediriger vers la page d'accueil
                return redirect('home')
            else:
                # Mot de passe incorrect
                messages.error(request, "Mot de passe incorrect")
        except RHUser.DoesNotExist:
            # Utilisateur non trouvé
            messages.error(request, "Aucun utilisateur trouvé avec cet email")

    return render(request, 'login/index.html')
#return render(request, 'login/index.html')

def home(request):
    return render(request, 'home.html')
