from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user),
    path('update', views.update_user),
    path('retrieve', views.retrieve_users),
    path('delete', views.delete_user),
]
