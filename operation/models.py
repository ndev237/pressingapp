from django.db import models
from ulid import ulid


class Commande(models.Model):
    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    client = models.ForeignKey('structure.Client', on_delete=models.SET_NULL, null=True)
    filiale = models.ForeignKey('structure.Filiale', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    prix = models.FloatField()


class Article(models.Model):
    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    client = models.ForeignKey('structure.Client', on_delete=models.SET_NULL, null=True)
    nombre = models.IntegerField()
    prix = models.FloatField()
    intitule = models.CharField(max_length=100)


class CommandeArticle(models.Model):
    comArt = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    quantite = models.IntegerField()
    montant = models.FloatField()


class Service(models.Model):
    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    intitule = models.CharField(max_length=20)


class LigneCommande(models.Model):
    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    intitule = models.CharField(max_length=100)

