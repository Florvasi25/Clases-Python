from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('prueba/', views.prueba, name='prueba'),
    path('segunda-vista', views.segunda_vista),
    path('crear-perro/<str:nombre>/<int:edad>/', views.crear_perro)
]
