from django.db import models
from django.conf import settings
from usuarios.models import User
from person.models import Person

from PIL import Image
import os
import platform

SO = platform.system()


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField("Ativo?", default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Imagem(models.Model):
    use_in_migrations = False
    imagem = models.ImageField()
    titulo = None

    src_root = 'media/images/' if SO == "Linux" else "media\\images\\"

    def salvar(self):
        img = Image.open(self.imagem)
        img.save(f'{self.src_root}{self.titulo}.png', 'PNG')

    def remover(self):
        os.remove(f'{self.src_root}{self.titulo}.png')


class Produto(Base):
    nome = models.CharField('Nome', max_length=50)
    preco = models.FloatField('Preço')
    quant = models.IntegerField("Quantidade")
    quant_minima = models.IntegerField("Quantidade Minima")
    imagem = None

    def __str__(self):
        return f"{self.nome} | R$ {self.preco} | {self.quant} Em Estoque"

    def load_image(self):
        try:
            src = f'images/p_{self.id}.png'
            img = Image.open('media/'+src)
            img.src = src
            self.imagem = img
        except FileNotFoundError:
            src = f'images/default.png'
            img = Image.open('media/'+src)
            img.src = src
            self.imagem = img

    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'preco': self.preco,
            'quant': self.quant,
            'quant_minima': self.quant_minima,
            'criado': self.criado,
            'modificado': self.modificado,
            'ativo': self.ativo,
            'user_id': str(self.user.id)
        }


class Venda(Base):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quant = models.IntegerField('Quantidade')
    desconto = models.FloatField('Desconto')
    cliente = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.produto} | {self.valor} | {self.quant}"

    @property
    def valor(self):
        return (self.produto.preco * self.quant) - self.desconto

    def to_json(self):
        return {
            'id': self.id,
            'valor': self.valor,
            'nome_produto': self.produto,
            'quant': self.quant,
            'desconto': self.desconto,
            'criado': self.criado,
            'modificado': self.modificado,
            'ativo': self.ativo,
            'cliente': self.cliente,
            'user_id': str(self.user.id)
        }

class Materiais(models.Model):
    id_material = models.AutoField(primary_key=True)
    nm_material = models.CharField(max_length=100)
    unidade = models.IntegerField(default=0)
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço")
    tipo = models.CharField(max_length=28, blank=True)
    validade_ca = models.DateField( blank=False, null=True, verbose_name="Data da Compra")
    localizacao = models.CharField(verbose_name="Local da Compra", max_length=100, blank=False, default='--')
    criado = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # alterando a exibição no painel do Admin
    def __str__(self):
        return f"{self.nm_material} | {self.preco_compra}"
