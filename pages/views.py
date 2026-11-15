from django.shortcuts import render
from .forms import ContactForm

def accueil(request):
    contexte = {
        "nom_projet": "BiblioLearn",
        "modules": ["Catalogue", "Comptes et rôles", "Emprunts", "Mini-cours"],
        "nb_ressources": 0,  
    }
    return render(request, "pages/accueil.html", contexte)
def a_propos(request):
    contexte = {
        "version": "1.0",
        "date_tp": "Novembre 2026",
    }
    return render(request, "pages/a_propos.html", contexte)

def contact(request):
    confirmation = ""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            confirmation = f"Merci {nom}, votre message a bien été reçu."
            form = ContactForm()
    else:
        form = ContactForm()
    
    contexte = {
        "form": form,
        "confirmation": confirmation,
    }
    return render(request, "pages/contact.html", contexte)