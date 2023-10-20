from django.urls import path
from . import views

app_name = 'localisation'
urlpatterns = [
    path('', views.index, name="localisation_index"),
    path('create_conti/', views.create_conti, name="continant_create"),
    path('update_conti/<str:pk>/', views.update_conti, name="continant_update"),
    path('delete_conti/<str:pk>/', views.delete_conti, name="continant_delete"),
    path('list_conti/', views.list_conti, name="continant_list"),
    path('create_pays/', views.create_pays, name="pays_create"),
    path('list_pays/', views.list_pays, name="pays_list"),
    path('update_pays/', views.update_pays, name="pays_update"),
    path('create_ville/', views.create_ville, name="ville_create"),
    path('list_ville/', views.list_ville, name="ville_list"),
    path('update_ville/', views.update_ville, name="ville_update"),
    path('create_quartier/', views.create_quartier, name="quartier_create"),
    path('update_quartier/', views.update_quartier, name="quartier_update"),
    path('list_quartier/', views.list_quartier, name="quartier_list"),
]
