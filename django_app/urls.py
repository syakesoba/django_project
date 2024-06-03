# Add File 2024/06/02

from django.urls import path
from django_app import views

# Add Start 2024/06/03
app_name = 'django_app'
# Add Start 2024/06/03

urlpatterns = [
    path('', views.index, name='index'), 
]