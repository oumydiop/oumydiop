from django.shortcuts import render
from .models import Etudiant, Cours, Absence

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'absences/liste_etudiants.html', {'etudiants': etudiants})

def liste_cours(request):
    cours = ["Python", "JavaScript", "Django", "Angular", "SQL", "ULM", "Wordpress", "Linux"]
    return render(request, 'absences\templates\index.html', {'cours': cours})

def enregistrer_absence(request):
    if request.method == 'POST':
        # Logique pour enregistrer l'absence
        pass
    else:
        # Afficher le formulaire d'enregistrement
        pass



# Create your views here.
