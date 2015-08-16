from django.contrib import admin
from .models import Cliente, Cobro, Venta

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellidos')


@admin.register(Cobro)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ()#'Cliente.nombre','Cliente.apellidos')


@admin.register(Venta)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ()#'Cliente.nombre','Cliente.apellidos')

