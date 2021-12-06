# from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
# from Cremeria_Toscano_1.models import Clientes
# # Register your models here.

from .models import *
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from Cremeria_Toscano_1.models import Clientes
#admin.site.register(Clientes)
admin.site.register(Compras)
admin.site.register(Detallescompras)
#admin.site.register(Productos)
admin.site.register(Ventas)
admin.site.register(Detallesventas)
admin.site.register(Proveedores)
#admin.site.register(Rutas)
#admin.site.register(Vendedores)

admin.site.site_header="Cremeria Toscano"
admin.site.site_title="Cremeria Toscano_1"
admin.site.index_title="Admon CT"

# class ClientesCT(admin.ModelAdmin): 
#   list_display=["idcliente","nombrecliente","idruta","adeudos"]
#   search_fields=["idcliente","nombrecliente"]
# pass

class VendedoresCT(admin.ModelAdmin): 
     list_display=["idvendedor","nombrev"]
     search_fields=["idvendedor","nombrev"]

class RutasCT(admin.ModelAdmin): 
     list_display=["idruta","idvendedor","detalleruta"]
     search_fields=["idruta"]

class ProductosCT(admin.ModelAdmin): 
    list_display=["idproducto","nombreproducto","cantidadp","precio","fechacaducidad"]
    search_fields=["idproducto", "nombreproducto","fechacaducidad"]



#admin.site.register(Clientes, ClientesCT)
admin.site.register(Vendedores, VendedoresCT)
admin.site.register(Rutas, RutasCT)
admin.site.register(Productos, ProductosCT)


#admin.py

 
@admin.register(Clientes)
class ClientesAdmin(ImportExportModelAdmin):
    list_display=["idcliente","nombrecliente","idruta","adeudos"]
    search_fields=["idcliente","nombrecliente"]
pass
