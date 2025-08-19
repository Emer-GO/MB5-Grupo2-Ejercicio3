from django.db import models

class Student(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    carrera = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
