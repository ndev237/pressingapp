from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Commande)
admin.site.register(CommandeArticle)
admin.site.register(Article)
admin.site.register(Service)
admin.site.register(LigneCommande)
