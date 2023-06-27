from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio),
    path('prueba/', views.prueba),
    path('segunda-vista', views.segunda_vista),
    path('crear-perro/<str:nombre>/<int:edad>/', views.crear_perro)
]
