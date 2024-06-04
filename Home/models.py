
from django.db import models

class Employe1(models.Model):
    matricule = models.CharField(primary_key=True, max_length=20)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    departement = models.CharField(max_length=100)
    date_embauche = models.DateField()
    date_naissance = models.DateField()
    email = models.EmailField()
    salaire = models.DecimalField(max_digits=10, decimal_places=2)

#class pour la liste des demandes de conge
class DemandeConge1(models.Model):
    employe = models.ForeignKey(Employe1, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    raison = models.CharField(max_length=100,default='')
    approuve = models.BooleanField(default=False)

#class employee,nbrprojet,jour abs non justif
class Performance(models.Model):
    employe = models.OneToOneField(Employe1, on_delete=models.CASCADE)
    projets_realises = models.IntegerField(default=0)
    assiduite = models.IntegerField(default=0)

   # def __str__(self):
    #    return f"Performance de {self.employe.nom}"


#class les employer qui doivent passer a la formation

class AppelFormation(models.Model):
    employe = models.ForeignKey(Employe1, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
     #   return f"Appel à la formation pour {self.employe.nom}"

#class table les demandes

class InfosCandidats(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    cv = models.FileField(upload_to='cvs/')
    motivation = models.FileField(upload_to='cvs/')
    approuve = models.BooleanField(default=False)
