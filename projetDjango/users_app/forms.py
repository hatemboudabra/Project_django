from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    nom = forms.CharField(max_length=30)
    prenom = forms.CharField(max_length=30)
    email = forms.EmailField()
    addresse = forms.CharField(max_length=100)

    USER_TYPES = [
        ('Client', 'Client'),
        ('Organisateur', 'Organisateur'),
        ('Admin', 'Admin')
    ]
    user_type = forms.ChoiceField(choices=USER_TYPES)

    lieu = forms.CharField(max_length=100, required=False, initial='Med')
    description = forms.CharField(max_length=100, required=False, initial='SEO')
    
    CATEGORIES = [
        ('LaLiga', 'LaLiga'),
        ('Serie A', 'Serie A'),
        ('Coupe du Monde', 'Coupe du Monde'),
        ('Champions League', 'Champions League'),
    ]
    categorie = forms.ChoiceField(choices=CATEGORIES, required=False, initial='Coupe du Monde')
