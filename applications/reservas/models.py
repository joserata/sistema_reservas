from django.db import models
from django.utils import timezone

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
    id = models.AutoField(primary_key=True) 
    imagen = models.CharField('imagen', max_length=255)
    name = models.CharField('Nombre', max_length=120)
    ubicacion = models.CharField('Ubicacion', max_length=50)
    capacidad = models.IntegerField()
    descripcion = models.CharField('Descripcion', max_length=255)
    estado = models.CharField('Estado', max_length=21)

    class Meta:
        managed = False  # Indica que Django no debe crear ni modificar la tabla en la DB
        db_table = 'espacios'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"{self.id} - {self.name} - {self.ubicacion} - {self.capacidad} - {self.descripcion} - {self.estado}"


class MetodosPago(models.Model):
    nombre_metodo = models.CharField('Nombre del metodo', max_length=50)
    class Meta:
        managed = False  # Indica que Django no debe crear ni modificar la tabla en la DB
        db_table = 'metodos_pago'

        def __str__(self):
            return f"{self.id} - {self.nombre_metodo}"


class HorariosDisponible(models.Model):
    id_horario = models.AutoField(primary_key=True)
    id_espacio = models.ForeignKey(Espacios, on_delete=models.CASCADE, db_column='id_espacio')  
    dia_semana = models.CharField('Día de la semana', max_length=20)
    hora_apertura = models.TimeField('Hora de apertura')
    hora_cierre = models.TimeField('Hora de cierre')

    class Meta:
        db_table = 'horarios_disponibles'  # Indicar la tabla ya existente en la base de datos

    def __str__(self):
        return f"{self.id_horario} - {self.dia_semana} ({self.hora_apertura} - {self.hora_cierre})"


class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True) 
    nombre_rol = models.CharField('Nombre', max_length=120)

    class Meta:
        db_table = 'roles'  

    def __str__(self):
        return f"{self.id} - {self.nombre_rol}"


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True) 
    nombre = models.CharField('Nombre', max_length=120)
    email = models.CharField('Email', max_length=21)
    password = models.CharField('password', max_length=30)
    id_rol = models.ForeignKey(Roles, on_delete=models.CASCADE, db_column='id_rol')  # Relación con roles
    direccion = models.CharField('Direccion', max_length=51)
    telefono = models.IntegerField

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.password} - {self.id_rol} - {self.direccion} - {self.telefono}"
    

class Reservas(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)
    comentarios = models.TextField()

    # Relaciones con otros modelos
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)  # Clave foránea para 'Usuarios'
    id_espacio = models.ForeignKey(Espacios, on_delete=models.CASCADE)  # Clave foránea para 'Espacios'

    class Meta:
        db_table = 'reservas'  # Asegúrate de que este nombre coincida con el de la tabla en la base de datos


    def __str__(self):
        return f"{self.id_reserva} - {self.fecha_reserva} {self.hora_inicio} - {self.id_usuario.nombre} - {self.id_espacio.name}"

  
class Pagos(models.Model):
       id_pago = models.AutoField(primary_key=True)
       id_reserva = models.ForeignKey(Reservas, on_delete=models.CASCADE, db_column='id_reserva')
       fecha_pago = models.DateTimeField
       monto = models.DecimalField
       id_metodo = models.ForeignKey(MetodosPago, on_delete=models.CASCADE, db_column='id_metodo_pago') 
       estado = models.CharField('Estado_pago', max_length=21)

       class Meta:
           db_table = 'pagos'
       def __str__(self):
           return f"{self.id_pago} - {self.id_reserva} - {self.fecha_pago} - {self.monto} - {self.id_metodo} - {self.estado}"

