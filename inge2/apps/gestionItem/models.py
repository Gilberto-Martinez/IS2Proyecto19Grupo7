from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager, 
    PermissionsMixin,
    Group)

# Create your models here.
class Proyecto(models.Model):
    id_proyecto = models.CharField(max_length=10)
    nombre = models.CharField(max_length=60)
    fases = (('A', 'Analisis'), ('D', 'Diseño'), ('C', 'Codificación'), ('P', 'Prueba'), ('M', 'Mantenimiento'))
    fase = models.CharField(max_length=13, choices=fases)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True)

    def __str__(self):
        return self.nombre


class LineaBase(models.Model):
    id_linea_base = models.CharField(max_length=10)
    enunciado = models.CharField(max_length=400)
    tarea = models.CharField(max_length=70)
    duenho_voluntario = models.CharField(max_length=60)
    estado = models.CharField(max_length=15)
    horas_estimadas = models.PositiveSmallIntegerField()
    id_proyecto = models.ForeignKey(Proyecto, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
            ordering = ['id']
            verbose_name_plural = 'Lineas Bases'

    def __str__(self):
        return self.id_linea_base


class PersonalizadoBaseUserManager(BaseUserManager):
    def create_user(self, usuario, password):
        user = self.model(usuario = usuario)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, password):
        user = self.create_user(self, usuario, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    usuario = models.CharField(max_length=40, unique=True, default='invitado')
    cedula_identidad = models.CharField(max_length=10) 
    nombre = models.CharField(max_length=40)
    correo = models.CharField(max_length=50)
    apellido = models.CharField(max_length=40)
    id_proyecto = models.ForeignKey(Proyecto, null=True, blank=False, on_delete=models.CASCADE)
    estados = (('A', 'Activo'), ('I', 'Inacivo'))
    estado = models.CharField(max_length=8, choices=estados)
    permiso = models.CharField(max_length=15)
    roles = (("A", "Administrador"), ("D", "Desarrollador"), ("P", "Product Owner"), ("S", "Scrum Master"))
    rol = models.CharField(max_length=15, choices=roles)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "usuario"
    objects = PersonalizadoBaseUserManager()

    def get_full_name(self):
        return self.usuario

    def get_short_name(self):
        return self.usuario

    def __str__(self):
        return self.usuario


class Item(models.Model):
    id_item = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=400)
    prioridades = (('A', 'Alta'), ('M', 'Media'), ('B', 'Baja'))
    prioridad = models.CharField(max_length=15, choices=prioridades)
    estado = models.CharField(max_length=15)
    atributo = models.CharField(max_length=20)
    version = models.CharField(max_length=10)
    observacion = models.CharField(max_length=400, blank= True)
    id_linea_base = models.ForeignKey(LineaBase, null=False, blank=False, on_delete=models.CASCADE)
    id_usuario_creador = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_item
