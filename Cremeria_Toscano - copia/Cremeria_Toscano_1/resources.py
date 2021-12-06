#resources.py
from import_export import resources
from .models import *
 
class ClientesResource(resources.ModelResource):
    class Meta:
        model = Clientes