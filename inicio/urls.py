from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # path('prueba/', views.prueba, name='prueba'),
    # path('segunda-vista', views.segunda_vista),
    #v1
    # path('crear-perro/<str:nombre>/<int:edad>/', views.crear_perro),
    #v2
    path('perros/', views.listar_perros, name='listar_perros'),
    path('perros/crear/', views.crear_perro, name='crear_perro'),
    path('perros/eliminar/<int:perro_id>/', views.eliminar_perro, name='eliminar_perro'),
    path('perros/modificar/<int:perro_id>/', views.modificar_perro, name='modificar_perro'),
]
