from django.db import models

# Create your models here.
class Tareas(models.Model):
    titulo = models.CharField()
    descripciom = models.CharField()
    fecha = models.DateField()

    def __str__(self):
        return self.titulo
