from django.db import models

class Notas(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    titulo = models.CharField(max_length=30)
    nota = models.PositiveSmallIntegerField()
    fecha = models.DateField()


    
