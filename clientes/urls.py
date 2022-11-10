from django.urls import path
from django.conf.urls import url,re_path
#from django.urls import re_path as url
from . import views
from clientes.models import Cad_Cliente, Info_cliente
from clientes.views import cadastrar_clientes_view,nome_clientes_view,cadastros_list,cadastro_enviado,cadastros_clientes_list,cadastro_clientes_enviado,export_data



app_name = 'clientes'

urlpatterns = [
    path('', views.cadastrar_clientes_view, name='clientes'),
    path('nome_clientes', views.nome_clientes_view, name='nome_clientes'),
    path('cadastros/cadastros_lista',views.cadastros_list, name='cadastros_lista'),
    re_path('cadastros/(?P<pk>[0-9]+)/$',views.cadastro_enviado,name='cadastro_detalhe'),
    path('cadastrospac/cadastros_clientes_lista',views.cadastros_clientes_list, name='cadastros_clientes_lista'),
    re_path('cadastrospac/(?P<pk>[0-9]+)/$',views.cadastro_clientes_enviado,name='cadastro_clientes_detalhe')
]