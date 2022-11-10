from django.urls import path
from .views import (index_estoque, cadastrar, buscar, editar, vender, listar, deletar, material)

urlpatterns = [
    path("listar/", listar, name="listar"),
    path("", index_estoque, name="index_estoque"),
    path("vender/", vender, name="vender"),
    path("cadastrar/", cadastrar, name="cadastrar"),
    path("material/", material, name="material"),
    path("buscar/", buscar, name="buscar"),
    path("editar/<str:pk>", editar, name="editar"),
    path("deletar/<str:pk>", deletar, name="deletar")
    #path("login/", logar_usuario, name="login"),
    #path("logout/", deslogar_usuario, name="logout")
]
