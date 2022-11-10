from django.contrib import admin
from .models import Produto, Venda, Materiais


class ProdutoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Produto, ProdutoAdmin)


class VendaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Venda, VendaAdmin)


class MateriaisAdmin(admin.ModelAdmin):
    pass

admin.site.register(Materiais, MateriaisAdmin)


# Register your models here.
