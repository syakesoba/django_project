# Add File 2024/06/02

from django.urls import path
from django_app import views

# Add Start 2024/06/03
app_name = 'django_app'
# Add Start 2024/06/03

urlpatterns = [
# Uodate Start 2024/06/05
#    path('', views.index, name='index'), 
    path('book/', views.index, name='index'),
# Update End   2024/06/05
# Add Start 2024/06/05
    path('book/add/', views.edit, name='add'),
    path('book/edit/(?P<id>\d+)/', views.edit, name='edit'),
    path('book/delete/(?P<id>\d+)/', views.delete, name='delete'),
    path('book/detail/(?P<id>\d+)/', views.detail, name='detail'),
# Add End   2024/06/05
]