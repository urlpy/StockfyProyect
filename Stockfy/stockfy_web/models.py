from django.db import models

# Create your models here.
from django.db import models

class Bien(models.Model):
    numero_inventario = models.CharField(max_length=50, unique=True)
    caracteristicas = models.TextField()
    marca = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    numero_serie = models.CharField(max_length=100, blank=True, null=True)
    estado_uso = models.CharField(max_length=100)
    costo_registrado = models.DecimalField(max_digits=12, decimal_places=2)
    area = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True, null=True)
    observaciones_adicionales = models.TextField(blank=True, null=True)
    observaciones_encargado = models.TextField(blank=True, null=True)

    foto_inmueble = models.ImageField(upload_to='inmuebles/', blank=True, null=True)
    foto_etiqueta = models.ImageField(upload_to='etiquetas/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Renombrar las fotos con el número de inventario
        if self.foto_inmueble:
            ext = self.foto_inmueble.name.split('.')[-1]
            self.foto_inmueble.name = f"{self.numero_inventario}_inmueble.{ext}"
        if self.foto_etiqueta:
            ext = self.foto_etiqueta.name.split('.')[-1]
            self.foto_etiqueta.name = f"{self.numero_inventario}_etiqueta.{ext}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.numero_inventario} - {self.marca} {self.modelo}"