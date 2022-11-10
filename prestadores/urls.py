from django.urls import path
#from django.conf.urls import url,re_path
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('cadastro-prestador-pf', views.cadastro_prestador_pf, name='cadastro_prestador_pf'),
    path('cadastro/dados-pessoais', views.dados_pessoais, name='dados_pessoais'),
    path('cadastro/cadastros_list',views.cadastros_list, name='cadastros_list'),
    path('cadastro/sucesso', views.sucesso2, name='sucesso'),
    path('cadastro/fornecedor',views.fornecedor, name='fornecedor'),
    re_path('cadastro/(?P<pk>[0-9]+)/$',views.cadastro_enviado,name='cadastro_prestadorpf')
]