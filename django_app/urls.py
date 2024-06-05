# Add File 2024/06/02

from django.urls import path
from django_app import admin, views

# Add Start 2024/06/03
app_name = 'django_app'
# Add Start 2024/06/03

urlpatterns = [
# Uodate Start 2024/06/05
#    path('', views.index, name='index'), 
    path('book/', views.index, name='index'),
# Add Uodate   2024/06/05
]