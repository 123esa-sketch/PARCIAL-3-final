from django.db import models
from django.contrib.auth.models import Group,User

Group.objects.get_or_create(name='Administrador')
Group.objects.get_or_create(name='Estudiante')

# TABLAS 
class ProveeFruta(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=80)
    direccion=models.CharField(max_length=200)
    telefono=models.CharField(max_length=12)
    correo_electronico=models.EmailField()

    def __str__(self):
        return self.nombre

class Fruta(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=80)
    tipo_fruta=models.CharField(max_length=80)
    origen=models.CharField(max_length=70)
    tempo_cultivo=models.DateField()
    precio=models.FloatField()
    cantidad=models.PositiveIntegerField()
    descripcion=models.CharField(max_length=200)
    proveedorid=models.ForeignKey(ProveeFruta, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=200)
    creacion=models.DateField()
    actualizacion=models.DateField()
    frutaid=models.ForeignKey(Fruta,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre