from django.contrib import admin
from .models import Cliente, Cobro, Venta

class ClienteAdmin(admin.ModelAdmin):
    fields = ["nombre","apellidos"]
admin.site.register(Cliente)
admin.site.register(Cobro)
admin.site.register(Venta)
