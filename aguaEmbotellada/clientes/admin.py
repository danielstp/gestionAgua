from django.contrib import admin
from .models import Cliente, Servicio, Venta
admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Venta)
