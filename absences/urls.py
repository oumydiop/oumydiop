from django.urls import path
from . import views

urlpatterns = [
    path('etudiants/', views.liste_etudiants, name='liste_etudiants'),
    path('cours/', views.liste_cours, name='listecour'),
    path('enregistrer-absence/', views.enregistrer_absence, name='enregistrer_absence'),
]
