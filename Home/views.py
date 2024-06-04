import os

from django.http import JsonResponse
#from django.contrib.auth.decorators import login_required
#from django.core.mail import send_mail

from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, Http404
from django.views.static import serve
#from django.conf import settings
from django.views.generic import View

from django.core.mail import send_mail
from pyexpat.errors import messages

from .models import DemandeConge1, Employe1, AppelFormation, Performance, InfosCandidats


def home(request):
    return render(request, 'home.html')


#def gerer_employe(request):
   # return render(request, 'gerer_employe.html')
def gerer_employe(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gerer_employe')
    else:
        form = EmployeForm()

    employes = Employe1.objects.all()

    context = {
        'employes': employes,
        'form': form,
    }
    return render(request, 'gerer_employe.html', context)

def supprimer_employe(request, employe_id):
    employe = Employe1.objects.get(matricule=employe_id)
    employe.delete()
    return redirect('gerer_employe')
def modifier_employe(request, employe_id):
    if request.method == 'POST':
        employe = Employe1.objects.get(id=employe_id)
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        employe = Employe1.objects.get(id=employe_id)
        form = EmployeForm(instance=employe)

        context = {
            'form': form,
        }
        return render(request, 'modifier_employe.html', context)
#def gerer_conge(request):
  #  return render(request, 'gerer_conge.html')




def gerer_conge(request):

    demandesconge = DemandeConge1.objects.using('GRH').all()

    if request.method == 'POST':

        demande_id = request.POST.get('demande_id')
        action = request.POST.get('action')

        if demande_id and action:
            demande = DemandeConge1.objects.using('GRH').get(pk=demande_id)
            if action == 'approuver':
                demande.approuve = True
                # Envoyer un e-mail à l'employé ap
                send_mail(
                    'Votre demande de congé a été approuvée',
                    'Votre demande de congé a été approuvée. Vous pouvez maintenant prendre vos congés aux dates demandées.',
                    'from@example.com',
                    [demande.employe.email],
                    fail_silently=False,
                )
            elif action == 'rejeter':
                demande.approuve = False
                # Envoyer un e-mail à l'employé rej
                send_mail(
                    'Votre demande de congé a été rejetée',
                    'Votre demande de congé a été rejetée. Veuillez contacter le service des ressources humaines pour plus d\'informations.',
                    'from@example.com',
                    [demande.employe.email],
                    fail_silently=False,
                )
            demande.save()

            return redirect('gerer_conge')

    return render(request, 'gerer_conge.html', {'demandesconge': demandesconge})




#def planifier_formation(request):
 #   return render(request, 'planifier_formation.html')
class PlanifierFormation(View):
    def get(self, request):

        appels_formation = AppelFormation.objects.using('GRH').all()
        return render(request, 'planifier_formation.html', {'appels_formation': appels_formation})



#def examiner_performance(request):
 #   return render(request, 'examiner_performance.html')

class ExaminerPerformance(View):
    def get(self, request):
       #la liste emp
        employes = Employe1.objects.using('GRH').all()
        for employe in employes:
            performance, created = Performance.objects.using('GRH').get_or_create(employe=employe)

            # Vérifier si l'employé répond aux critères de formation
            if performance.projets_realises < 3 or performance.assiduite < 100:  # Exemple de critères
                AppelFormation.objects.using('GRH').get_or_create(employe=employe)

      #liste perf
        employes_performances = Performance.objects.using('GRH').select_related('employe').all()

        return render(request, 'examiner_performance.html', {'employes_performances': employes_performances})

class EnvoyerEmailFormation(View):
    def post(self, request):
        employe_id = request.POST.get('matricule')


        employe = Employe1.objects.using('GRH').get(id=employe_id)

        # Envoyer un email à l'employé
        send_mail(
            'Formation à suivre',
            'Bonjour {},\n\nVous êtes convoqué à une formation.\n\nCordialement,\nVotre entreprise'.format(employe.nom),
            'charraimanel@gmail.com',  # Remplacez par votre adresse email d'envoi
            [employe.email],  # Envoyer à l'employé concerné
        )

        # Répondre avec un JSON pour indiquer que l'e-mail a été envoyé avec succès
        return JsonResponse({'success': True})

#def examiner_candidature(request):
 #  return render(request, 'examiner_candidature.html')




from django.http import JsonResponse


def examiner_candidature(request):
    candidatures = InfosCandidats.objects.using('GRH').all()

    if request.method == 'POST':
        candidature_id = request.POST.get('candidature_id')
        action = request.POST.get('action')

        if candidature_id and action:
            candidature = InfosCandidats.objects.using('GRH').get(pk=candidature_id)
            if action == 'Accepter':
                candidature.Accepter = True
                # Envoyer un e-mail au candidat
                send_mail(
                    'Votre candidature a été acceptée',
                    'Félicitations ! Votre candidature a été acceptée. Vous recevrez bientôt un appel pour un entretien téléphonique.',
                    'from@example.com',
                    [candidature.email],
                    fail_silently=False,
                )
            elif action == 'Rejeter':
                messages.success(request, 'L\'e-mail de rejet a été envoyé avec succès.')
                candidature.Accepter = False

                send_mail(
                    'Votre candidature a été refusée',
                    'Votre candidature a été refusée. Nous vous remercions pour l\'intérêt que vous avez porté à notre entreprise.',
                    'charraimanel@gmail.com',
                    [candidature.email],
                    fail_silently=False,
                )
            candidature.save()

            return redirect('examiner_candidature')

    return render(request, 'examiner_candidature.html', {'candidatures': candidatures})





#def examiner_candidature(request):
 #   candidatures = InfosCandidats.objects.using('GRH').all()
  #  return render(request, 'examiner_candidature.html', {'candidatures': candidatures})

def telecharger_pdf(request, path):
    print("Chemin du fichier PDF:", path)

    pdf_path = os.path.join(settings.MEDIA_ROOT, path)
    print("Chemin absolu du fichier PDF:", pdf_path)

    try:
        return serve(request, os.path.basename(pdf_path), os.path.dirname(pdf_path))
    except Http404:
        print("Fichier non trouvé")
        return HttpResponse("Fichier non trouvé", status=404)

"""
def examiner_candidature(request):
    # Suppose que vous avez récupéré un objet InfosCandidats nommé candidature
    candidature = InfosCandidats.objects.using('GRH').get(pk=1)
    pdf_url = settings.MEDIA_URL + candidature.cv.url
    return render(request, 'examiner_candidature.html', {'pdf_url': pdf_url})"""