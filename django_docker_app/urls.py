from django.urls import path
from django_docker_app import views

urlpatterns = [
    path('', views.index, name='index'), 
]