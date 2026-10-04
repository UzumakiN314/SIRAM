from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Organismo
class Organismo(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# Usuario relacionado con Organismo
class Usuario(AbstractUser):
    organismo = models.ForeignKey(Organismo, on_delete=models.SET_NULL, null=True, blank=True)

# 2. Estado
class Estado(models.Model):
    nombre = models.CharField(max_length=50, unique=True) # PENDIENTE, VALIDADA, RECHAZADA, etc.

    def __str__(self):
        return self.nombre

# 3. Víctima
class Victima(models.Model):
    nombre = models.CharField(max_length=150, blank=True, null=True)
    contacto = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.nombre or f"Víctima #{self.id}"

# 4. Animal
class Animal(models.Model):
    especie = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    def __str__(self):
        return f"{self.especie} - #{self.id}"

# 5. Caso (Unidad consolidada)
class Caso(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='casos')
    animales = models.ManyToManyField(Animal, related_name='casos', blank=True)

    def __str__(self):
        return f"Caso #{self.id}"

# 6. Denuncia
class Denuncia(models.Model):
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fuente = models.CharField(max_length=100) # Municipal, Provincial, Externa, etc.
    descripcion = models.TextField()
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='denuncias')
    victima = models.ForeignKey(Victima, on_delete=models.SET_NULL, null=True, blank=True, related_name='denuncias')
    animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True, blank=True, related_name='denuncias_informadas')
    caso = models.ForeignKey(Caso, on_delete=models.SET_NULL, null=True, blank=True, related_name='denuncias_asociadas')

    def __str__(self):
        return f"Denuncia #{self.id} ({self.fuente})"

# 7. Historial de Auditoría
class HistorialAuditoria(models.Model):
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE, related_name='historial')
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    accion = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return f"Auditoría Caso #{self.caso.id} - {self.fecha_hora}"


