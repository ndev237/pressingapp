from django.urls import path
from .import views

app_name = 'operation'

urlpatterns = [
    path('', views.index, name="operation_index"),
    path('add_commande/', views.add_commande, name="commande_add"),
    path('update_commande/<str:pk>/', views.update_commande, name="commande_update"),
    path('delete_commande/<str:pk>/', views.delete_commande, name="commande_delete"),
    path('list_commande/', views.list_commande, name="commande_list"),
    path('add_article/', views.add_article, name="article_add"),
    path('update_article/<str:pk>/', views.update_article, name="article_update"),
    path('delete_article/<str:pk>/', views.delete_article, name="article_delete"),
    path('list_article/', views.list_article, name="article_list"),
    path('add_service/', views.add_service, name="service_add"),
    path('update_service/<str:pk>/', views.update_service, name="service_update"),
    path('delete_service/<str:pk>/', views.delete_service, name="service_delete"),
    path('list_service/', views.list_service, name="service_list"),
    path('add_comart/', views.add_comart, name="comart_add"),
    path('update_comart/<str:pk>/', views.update_comart, name="comart_update"),
    path('delete_comart/<str:pk>/', views.delete_comart, name="comart_delete"),
    path('list_comart/', views.list_comart, name="comart_list"),
    path('add_ligncom/', views.add_ligncom, name="ligncom_add"),
    path('update_ligncom/<str:pk>/', views.update_ligncom, name="ligncom_update"),
    path('delete_ligncom/<str:pk>/', views.delete_ligncom, name="ligncom_delete"),
    path('list_ligncom/', views.list_ligncom, name="ligncom_list"),
]