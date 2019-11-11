from django.contrib import admin
from inge2.apps.gestionItem.models import *
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AdminProyecto(admin.ModelAdmin):
    list_display = ["id_proyecto", "nombre", "fase", "fecha_inicio", "fecha_fin"]
    list_filter = ["nombre"]
    list_editable = ["nombre", "fase", "fecha_inicio", "fecha_fin"]
    search_fields = ["nombre"]

"""class AdminUsuario(admin.ModelAdmin):
    list_display = ["cedula_identidad", "nombre", "apellido", "estado", "rol"]
    list_filter = ["nombre"]
    list_editable = ["nombre", "apellido", "estado", "rol"]
    search_fields = ["nombre"]"""

class PersonalizadoUserAdmin(UserAdmin):
	fieldsets = ()
	add_fields = ((None, {
		'fields': ('usuario', 'password1', 'password2')
		}))
	list_display = ["usuario", "nombre", "apellido", "estado", "rol"]
	list_filter = ["usuario"]
	search_fields = ["usuario"]
	ordering = ["usuario"]

admin.site.register(Proyecto, AdminProyecto)
admin.site.register(LineaBase)
admin.site.register(Usuario, PersonalizadoUserAdmin)
admin.site.register(Item)
