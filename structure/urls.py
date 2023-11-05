from django.urls import path
from . import views

app_name = 'structure'
urlpatterns = [
    path('', views.index, name="structure_index"),
    path('create_user/', views.create_user, name="user_create"),
    path('update_user/<str:pk>/', views.update_user, name="user_update"),
    path('delete_user/<str:pk>/', views.delete_user, name="user_delete"),
    path('list_user/', views.list_user, name="user_list"),
    path('create_entreprise/', views.create_entreprise, name="entreprise_create"),
    path('update_entreprise/<str:pk>/', views.update_entreprise, name="entreprise_update"),
    path('delete_entreprise/<str:pk>/', views.delete_entreprise, name="entreprise_delete"),
    path('list_entreprise/', views.list_entreprise, name="entreprise_list"),
    path('add_filiale/', views.create_filiale, name="filiale_add"),
    path('update_filiale/<str:pk>/', views.update_filiale, name="filiale_update"),
    path('delete_filiale/<str:pk>/', views.delete_filiale, name="filiale_delete"),
    path('list_filiale/', views.list_filiale, name="filiale_list"),
    path('create_client/', views.create_client, name="client_create"),
    path('update_client/<str:pk>/', views.update_client, name="client_update"),
    path('delete_client/<str:pk>/', views.delete_client, name="client_delete"),
    path('list_client/', views.list_client, name="client_list"),
]
