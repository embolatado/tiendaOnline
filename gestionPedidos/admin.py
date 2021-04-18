from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# CREAR VISTAS PERSONALIZADAS PARA EL PANEL DE ADMINISTRACIÓN.
class panelClientes(admin.ModelAdmin):
    list_display=('nombre', 'email', 'tfno')
    search_fields = ("nombre", "tfno")

# Register your models here Y LAS VISTAS PERSONALIZADAS DEL /ADMIN
admin.site.register(Clientes, panelClientes)
admin.site.register(Articulos)
admin.site.register(Pedidos)
