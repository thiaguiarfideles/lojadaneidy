from django.db import models
from django.conf import settings
from usuarios.models import User
from person.models import Person
from django_prices.models import MoneyField, TaxedMoneyField
from datetime import datetime
from decimal import *

from PIL import Image
import os
import platform

SO = platform.system()

STATUS_PAGAMENTO = (
    ('CARTÃO_CREDITO', 'Cartão de credito'),
    ('DINHEIRO', 'Dinheiro'),
    ('PIX', 'Pix'),    
)

STATUS_INGREDIENTE = (
    ('1_litro', '1_LITRO'),
    ('2_litro', '2_LITRO'),
    ('600_Ml', '600_Ml'),
    ('300_Ml', '300_Ml'),
    ('300_Ml', '300_Ml'),
    ('200_Ml', '200_Ml'),
    ('100_Ml', '100_Ml'),
    ('1_KILO', '1_KILO'),
    ('3_KILOS', '3_KILOS'), 
    ('5_KILOS', '5_KILOS'), 
    ('10_KILOS', '10_KILOS'), 
    ('100_g', '100_g'),
    ('200_g', '200_g'), 
    ('300_g', '300_g'), 
    ('500_g', '500_g'),
    ('1_un', '1_un'), 
    ('2_un', '2_un'), 
    ('3_un', '3_un'), 
    ('5_un', '5_un'),
    ('10_un', '10_un'), 

)


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
    unidade = models.CharField(max_length=300, default="500_GRAMAS", choices=STATUS_INGREDIENTE)
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço", default=Decimal('0.00'), help_text ="Inserir preço de compra do produto")
    tipo = models.CharField(max_length=28, blank=True, default='INGREDIENTE')
    validade_ca = models.DateField(help_text = "Inserir data neste formato: <em>DD/MM/YYYY</em>.", default=datetime.now, blank=True, null=True, verbose_name="Data da Compra")
    localizacao = models.CharField(verbose_name="Local da Compra", max_length=100, blank=False, default='GUANABARA')
    criado = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.CharField(verbose_name="Tipo de Pagamento", max_length=30, default="Cartão de Credito", choices=STATUS_PAGAMENTO)

    # alterando a exibição no painel do Admin
    def __str__(self):
        return f"{self.nm_material} | {self.preco_compra}"
