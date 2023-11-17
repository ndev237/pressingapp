from .models import User, Entreprise, Filiale, Client, Message
from django.contrib.auth.forms import *
from django.contrib.auth import get_user_model


class UserForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['last_name', 'first_name', 'username', 'email', 'password']


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
        fields = ['user', 'nom', 'prenom', 'sex', 'adresse', 'email', 'tel']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['nom', 'tel', 'email', 'message']
