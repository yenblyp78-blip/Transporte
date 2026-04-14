from django.contrib import admin
from .models import Bus, Pasajero, Viaje, Ruta, Boleto

# Register your models here.
admin.site.register(Bus)
admin.site.register(Pasajero)
admin.site.register(Viaje)
admin.site.register(Ruta)
admin.site.register(Boleto)