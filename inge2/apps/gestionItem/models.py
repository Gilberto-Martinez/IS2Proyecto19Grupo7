from django.db import models

# Create your models here.
class Proyecto(models.Model):
    id_proyecto = models.CharField(max_length=10)
    nombre = models.CharField(max_length=60)
    fase = models.CharField(max_length=10)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True)

    def __str__(self):
        return self.nombre

class LineaBase(models.Model):
    id_linea_base = models.CharField(max_length=10)
    estado = models.CharField(max_length=10)
    enunciado = models.CharField(max_length=400)
    tarea = models.CharField(max_length=50)
    duenho_voluntario = models.CharField(max_length=60)
    horas_estimadas = models.PositiveSmallIntegerField()
    id_proyecto = models.ForeignKey(Proyecto, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_linea_base

class Usuario(models.Model):
    cedula_identidad = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.CharField(max_length=50)
    contrasenha = models.CharField(max_length=20)
    id_proyecto = models.ForeignKey(Proyecto, null=False, blank=False, on_delete=models.CASCADE)
    estado = models.CharField(max_length=8)
    permiso = models.CharField(max_length=15)
    rol = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre +" "+ self.apellido

class Item(models.Model):
    id_item = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=400)
    prioridad = models.CharField(max_length=10)
    estado = models.CharField(max_length=10)
    atributo = models.CharField(max_length=20)
    version = models.CharField(max_length=10)
    observacion = models.CharField(max_length=400)
    id_linea_base = models.ForeignKey(LineaBase, null=False, blank=False, on_delete=models.CASCADE)
    id_usuario_creador = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    # archivo_externo

    def __str__(self):
        return self.id_item
