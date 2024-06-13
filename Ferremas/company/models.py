from django.db import models

class Sede(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField( max_length=100)
    direccion = models.CharField( max_length=100)

class Empleado(models.Model):
    run = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=100,unique=True)
    tipo =models.CharField(max_length=50)
    contrasenya = models.CharField(max_length=20)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField( max_length=50, unique=True)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(null=False)
    precio = models.PositiveIntegerField(null=False)
    descuento = models.PositiveSmallIntegerField(null= True)
    sede = models.ForeignKey(Sede,on_delete=models.CASCADE)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=500)


class Pedido(models.Model):
    codigo = models.AutoField(primary_key=True)
    empleado = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_prep =models.DateTimeField(null=True) #! preparacion
    fecha_extr =models.DateTimeField(null=True) #! extraccion
    fecha_desp =models.DateTimeField(null=True) #! despacho
    fecha_entr =models.DateTimeField(null=True) #! entrega
    estado = models.CharField(max_length=30)
    compra = models.CharField(max_length=50) #! foreing key de compra.