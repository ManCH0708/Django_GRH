from django.urls import path
from Home import views
from Home.views import ExaminerPerformance, PlanifierFormation, EnvoyerEmailFormation, examiner_candidature
    #telecharger_pdf, \

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/gerer_employe/', views.gerer_employe, name='gerer_employe'),
    path('home/gerer_conge/', views.gerer_conge, name='gerer_conge'),
    #path('home/planifier_formation/', views.planifier_formation, name='planifier_formation'),
    path('home/planifier_formation/', PlanifierFormation.as_view(), name='planifier_formation'),
    path('home/envoyer_email/', EnvoyerEmailFormation.as_view(), name='envoyer_email'),
    path('home/download/<path:path>/', views.telecharger_pdf, name='download_pdf'),
    #path('home/examiner_performance/', views.ExaminerPerformance, name='examiner_performance'),
    path('home/examiner_performance/', ExaminerPerformance.as_view(), name='examiner_performance'),
    path('home/examiner_candidature/', views.examiner_candidature, name='examiner_candidature'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



