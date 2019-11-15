from django.contrib import admin
from inge2.apps.gestionItem.models import *
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AdminLineaBase(admin.ModelAdmin):
    list_display = ["id_linea_base", "enunciado", "tarea", "duenho_voluntario", "estado",
					"horas_estimadas", "id_proyecto"]
    list_filter = ["id_linea_base"]
    list_editable = ["enunciado", "tarea", "duenho_voluntario", "estado",
					"horas_estimadas", "id_proyecto"]
    search_fields = ["id_linea_base"]

class AdminProyecto(admin.ModelAdmin):
    list_display = ["id_proyecto", "nombre", "fase", "fecha_inicio", "fecha_fin"]
    list_filter = ["nombre"]
    list_editable = ["nombre", "fase", "fecha_inicio", "fecha_fin"]
    search_fields = ["nombre"]

class PersonalizadoUserAdmin(UserAdmin):
	fieldsets = ()
	add_fields = ((None, {
		'classes': ('wide',),
		'fields': ('usuario', 'password1', 'password2')
		}))
	list_display = ["usuario", "nombre", "apellido", "estado", "rol"]
	list_filter = ["usuario"]
	search_fields = ["usuario"]
	ordering = ["usuario"]

class AdminItem(admin.ModelAdmin):
    list_display = ["id_item", "descripcion", "estado", "id_linea_base", "id_usuario_creador",]
    list_filter = ["id_item"]
    list_editable = ["descripcion", "estado", "id_linea_base", "id_usuario_creador",]
    search_fields = ["id_item"]

admin.site.register(Proyecto, AdminProyecto)
admin.site.register(LineaBase, AdminLineaBase)
admin.site.register(Usuario, PersonalizadoUserAdmin)
admin.site.register(Item, AdminItem)
