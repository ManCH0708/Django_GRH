from django.urls import path
from Login import views

urlpatterns = [
    path('', views.login, name='login'),


]
