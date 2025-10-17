from django.db import models
from django.contrib.auth.models import AbstractUser

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre



class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            ("ProductoListView", "Puede ver la sección de productos"),            
        ]   
