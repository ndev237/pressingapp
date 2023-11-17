from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from ulid import ulid


# Create your models here.
class User(AbstractUser):
    class Sex(models.TextChoices):
        MAN = 'Homme', _('Homme')
        WOMAN = 'Femme', _('Femme')

    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    sex = models.CharField(choices=Sex.choices, null=False, max_length=10)

    def get_full_name(self):
        return f"{self.first_name}{self.last_name}"

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')


class Entreprise(models.Model):
    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    nom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=20)
    tel = models.IntegerField()


class Filiale(models.Model):
    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.SET_NULL, null=True)
    ville = models.ForeignKey('localisation.Ville', on_delete=models.SET_NULL, null=True)
    nom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=20)
    tel = models.IntegerField()


class Client(models.Model):
    class Sex(models.TextChoices):
        MAN = 'Home', _('Homme')
        WOMAN = 'Femme', _('Femme')

    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    sex = models.CharField(choices=Sex.choices, null=False, max_length=12)
    adresse = models.CharField(max_length=10)
    email = models.EmailField(max_length=40)
    tel = models.IntegerField()


class Message(models.Model):
    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    nom = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)
    tel = models.IntegerField()
    message = models.CharField(max_length=255)