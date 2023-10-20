from django import forms
from .models import User, Entreprise, Filiale, Client


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'sex', 'username', 'email', 'groups', 'user_permissions']


class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ['nom', 'adresse', 'tel']


class FilialeForm(forms.ModelForm):
    class Meta:
        model = Filiale
        fields = ['entreprise', 'ville', 'nom', 'adresse', 'tel']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user', 'nom', 'prenom', 'adresse', 'email', 'tel']
