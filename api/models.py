from django.db import models

# Create your models here.


class Venture(models.Model):
    uuid = models.UUIDField(unique=True)
    productTitle = models.CharField(max_length=255)

    def __str__(self):
        return self.productTitle


class Cita(models.Model):
    nombre = models.CharField(max_length=255)
    celular = models.CharField(max_length=15)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    status = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    venture = models.ForeignKey(
        Venture, on_delete=models.CASCADE)  # Relación con Venture

    def __str__(self):
        return self.nombre
