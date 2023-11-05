from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from ulid import ulid


# Create your models here.
class User(AbstractUser):
    class Sex(models.TextChoices):
        MAN = 'man', _('Homme')
        WOMAN = 'Woman', _('Femme')

    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    sex = models.CharField(choices=Sex.choices, null=False, max_length=12)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    groups = models.ManyToManyField('auth.group', related_name='custom_user_group')
    user_permissions = models.ManyToManyField('auth.permission', related_name='custom_user_permission')


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
    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    adresse = models.CharField(max_length=10)
    email = models.EmailField(max_length=40)
    tel = models.IntegerField()
