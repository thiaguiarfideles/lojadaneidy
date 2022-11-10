#coding: utf-8

import uuid
from uuid import uuid4
from django.db import models
from django.utils import timezone
from usuarios.models import User
from prestadores.models import Especialidade
from core.helpers import validate_file_extension
from address.models import AddressField
import datetime




class Cad_Cliente(models.Model):
    nm_cliente = models.CharField(max_length=200, blank=True, null=True)
    #models.AutoField(primary_key=True)
    def __str__(self):
        return str(self.nm_cliente)



class Info_cliente(models.Model):
    cliente = models.ForeignKey(Cad_Cliente, related_name='%(class)s_requests_created', on_delete = models.CASCADE, verbose_name="Nome Cliente")
    email = models.EmailField(verbose_name="Email", max_length=200, blank=True, null=True)
    ds_endereco = AddressField(on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Endereço")
    cidade = models.CharField(verbose_name="Cidade", max_length=200, blank=True, null=True)
    cep = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField(null=True)
    sexo = models.IntegerField(choices=((1, 'Masculino'), (2, 'Feminino')), null=True)
    telefone = models.CharField(max_length=11, blank=True, null=False)
    comentarios = models.TextField(blank=True, null=True,verbose_name="Comentarios")
    date_add = models.DateTimeField(default = timezone.now)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,related_name='+',)
    id_cliente = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return "%s" % self.cliente        





