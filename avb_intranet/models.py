from django.db import models

# Create your models here.

class RecintoLiceo(models.Model):
    nombre = models.CharField(max_length=100)
    pabellon = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - Pabellón {self.pabellon}"

class AnuncioInstitucional(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo