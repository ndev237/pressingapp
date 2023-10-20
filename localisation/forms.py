from django import forms
from .models import Continant, Pays, Ville, Quartier


class ContinantForm(forms.ModelForm):
    class Meta:
        model = Continant
        fields = ['intitule']


class PaysForm(forms.ModelForm):
    class Meta:
        model = Pays
        fields = ['continant', 'intitule']


class VilleForm(forms.ModelForm):
    class Meta:
        model = Ville
        fields = ['pays', 'intitule']


class QuartierForm(forms.ModelForm):
    class Meta:
        model = Quartier
        fields = ['ville', 'intitule']
