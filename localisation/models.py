from django.db import models
from ulid import ulid
from django.urls import reverse


class Continant(models.Model):
    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    intitule = models.CharField(max_length=30)


class Pays(models.Model):
    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    continant = models.ForeignKey(Continant, on_delete=models.CASCADE)
    intitule = models.CharField(max_length=30)


class Ville(models.Model):
    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    pays = models.ForeignKey(Pays, on_delete=models.SET_NULL, null=True)
    intitule = models.CharField(max_length=30)


class Quartier(models.Model):
    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    ville = models.ForeignKey(Ville, on_delete=models.SET_NULL, null=True)
    intitule = models.CharField(max_length=30)
