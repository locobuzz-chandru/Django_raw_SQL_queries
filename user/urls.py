from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user),
    path('update', views.update_user),
    path('retrieve', views.retrieve_users),
    path('delete', views.delete_user),
    path('retrieve_data', views.retrieve),
    path('add_city', views.add_city),
    path('delete_city', views.delete_city),
]
