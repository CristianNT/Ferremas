from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=100,unique=True)
    contrasenya = models.CharField(max_length=20)
    direccion = models.CharField( max_length=100)
    
class Compra(models.Model):
    codigo = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=50)
    empleado = models.CharField(max_length=50)
    fecha =  models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(null=False) #! Aqui van los productos y los subtotales
    total = models.PositiveIntegerField(null=False)
    ubicacion = models.CharField( max_length=100)
