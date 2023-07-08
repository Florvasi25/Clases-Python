from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=20) 
    edad = models.IntegerField()
    descripcion = models.TextField(null=True)

    def __str__(self):
        return f"Perro: {self.nombre} - Edad: {self.edad}"