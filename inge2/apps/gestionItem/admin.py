from django.contrib import admin
from inge2.apps.gestionItem.models import *
from .models import *

# Register your models here.

class AdminProyecto(admin.ModelAdmin):
    list_display = ["id_proyecto", "nombre", "fase", "fecha_inicio", "fecha_fin"]
    list_filter = ["nombre"]
    list_editable = ["nombre", "fase", "fecha_inicio", "fecha_fin"]
    search_fields = ["nombre"]

class AdminUsuario(admin.ModelAdmin):
    list_display = ["cedula_identidad", "nombre", "apellido", "estado", "rol"]
    list_filter = ["nombre"]
    list_editable = ["nombre", "apellido", "estado", "rol"]
    search_fields = ["nombre"]

admin.site.register(Proyecto, AdminProyecto)
admin.site.register(LineaBase)
admin.site.register(Usuario, AdminUsuario)
admin.site.register(Item)
