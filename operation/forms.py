from django import forms
from .models import Commande, Article, CommandeArticle, Service, LigneCommande


class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['client', 'filiale', 'date', 'prix']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['client', 'nombre', 'prix', 'intitule']


class CommandeArticleForm(forms.ModelForm):
    class Meta:
        model = CommandeArticle
        fields = ['commande', 'article', 'quantite', 'montant']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['intitule']


class LigneCommandeForm(forms.ModelForm):
    class Meta:
        model = LigneCommande
        fields = ['commande', 'service', 'intitule']
