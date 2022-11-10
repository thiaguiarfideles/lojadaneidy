import uuid
from uuid import uuid4
from django.db import models
from django.contrib import admin 
from django.conf import settings
from django.utils import timezone
from usuarios.models import User
from django.contrib.contenttypes.models import ContentType

from address.models import AddressField


import datetime


class Person(models.Model):
    """Model definition for Person."""

    address = AddressField(on_delete=models.CASCADE, verbose_name = 'Endereço')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='+',)
    complemento = models.CharField(verbose_name="Complemento", max_length=200, blank=True, null=True)
    date_add = models.DateTimeField(default = timezone.now)
    cliente = models.CharField(verbose_name="Nome Cliente", max_length=200, blank=True, null=True)
    email = models.EmailField(verbose_name="Email", max_length=200, blank=True, null=True)
    idade = models.IntegerField(null=True)
    sexo = models.IntegerField(choices=((1, 'Masculino'), (2, 'Feminino')), null=True)
    telefone = models.CharField(max_length=11, blank=True, null=False)

    class Meta:
        """Meta definition for Person."""

        verbose_name = 'Endereço Cliente'
        verbose_name_plural = 'Endereço Clientes'

    def __str__(self):
        """Unicode representation of Person."""
        return "%s" % self.cliente
