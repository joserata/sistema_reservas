from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shorname = models.CharField('Nombre corto', max_length=30)
    anulate = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return self.id + '-' + self.name + '-' + self.shorname
        


class Datos(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    direccion = models.CharField('Direccion', max_length=50)
    telefono = models.CharField('Telefono', max_length=21)

    def __str__(self):
        return self.id + '-' + self.nombre + '-' + self.apellidos + '-' + self.direccion + '-', + self.telefono       
    

class Espacios(models.Model):
    nombre = models.CharField('Nombre', max_length=120)
    ubicacion = models.CharField('Ubicacion', max_length=50)
    capacidad = models.IntegerField()
    descripcion = models.CharField('Descripcion', max_length=255)
    estado = models.CharField('Estado', max_length=21)

    class Meta:
        managed = False  # Indica que Django no debe crear ni modificar la tabla en la DB
        db_table = 'espacios'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.ubicacion} - {self.capacidad} - {self.descripcion} - {self.estado}"
    