from django.db import models
from ulid import ulid


class Message(models.Model):
    id = models.CharField(primary_key=True, max_length=30, default=ulid, editable=False, db_index=True)
    nom = models.CharField(max_length=50)
    tel = models.IntegerField()
    email = models.EmailField()
    message = models.CharField(max_length=255)
