from import_export import resources
from clientes.models import Cad_Cliente, Info_cliente

class Cad_ClienteResource(resources.ModelResource):
    class Meta:
        model = Cad_Cliente

class Info_clienteResource(resources.ModelResource):
    class Meta:
        model = Info_cliente        