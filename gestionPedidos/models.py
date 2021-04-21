from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre de Cliente")
    direccion = models.CharField(max_length=50) 
    email = models.EmailField(blank = True, null = True, verbose_name="Correo electrónico")
    tfno = models.CharField(max_length=9, verbose_name="Teléfono")
    
    # DEFINIR QUÉ QUEREMOS VER
    def __str__(self):
      return self.nombre


class Articulos(models.Model):
  nombre = models.CharField(max_length=30)
  seccion = models.CharField(max_length=20)
  precio = models.IntegerField()

  def __str__(self):
    return 'El artículo %s de la sección %s cuesta %s€' % (self.nombre, self.seccion, self.precio)


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
