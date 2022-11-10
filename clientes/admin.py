from import_export.admin import ImportExportModelAdmin
from django.contrib import admin


from clientes.models import Cad_Cliente, Info_cliente

from import_export import resources


class AdminCad_Cliente(admin.ModelAdmin):
	list_display = ['nm_cliente']

admin.site.register(Cad_Cliente, AdminCad_Cliente)

class AdminInfo_cliente(admin.ModelAdmin):
	list_display = ['cliente', 'ds_endereco', 'telefone']

admin.site.register(Info_cliente, AdminInfo_cliente)

