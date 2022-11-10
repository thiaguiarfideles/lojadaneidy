from django import forms
from django_prices.forms import MoneyField
from .models import Produto, Venda, Materiais
from person.models import Person


class ModeloCharField(forms.CharField):
    def __init__(self, name="", ml=35, **kwargs):
        super().__init__(**kwargs, max_length=ml, label='', widget=forms.TextInput(
            attrs={'placeholder': f'{name}', 'style': 'margin: 1% 0'}
        ))


class ModeloIntegerField(forms.IntegerField):
    def __init__(self, name="", required=True, **kwargs):
        super().__init__(**kwargs, label='', required=required, widget=forms.TextInput(
            attrs={'placeholder': f'{name}', 'style': 'margin: 1% 0'}
        ))


class ModeloDecimalField(forms.DecimalField):
    def __init__(self, name="", required=True, **kwargs):
        super().__init__(**kwargs, label='', required=required, widget=forms.TextInput(
            attrs={'placeholder': f'{name}', 'style': 'margin: 1% 0'}
        ))


class ImagemModelForm(forms.Form):
    imagem = forms.ImageField(
        label='Select a Image',
        help_text='max. 42 megabytes',
        required=False
    )


def get_produto_json(nome_produto):
    produto = Produto.objects.filter(nome__icontains=nome_produto)
    return produto[0].to_json() if produto else produto


def get_produtos_json(nome_produto):
    produtos = list(filter(lambda x: f"{nome_produto}" in x.to_json()["nome"], list(Produto.objects.all())))
    return produtos


def get_produtos_produto(nome_produto, user_creator):
    return Produto.objects.filter(nome__icontains=nome_produto, user=user_creator)


def checar_produto(nome_produto, quant=-1):
    produto_json = get_produto_json(nome_produto)
    if nome_produto == 'default':
        return 500
    if produto_json:
        if int(produto_json["quant"]) >= quant:
            return 200
        else:
            return 500
    return 404


class ProdutoModelForm(forms.ModelForm):
    def registrar(self, user):
        p = self.save(commit=False)
        p.user = user
        p.save()
        return p.id

    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'quant', 'quant_minima']
        labels = {
            'nome': "",
            'preco': "",
            'quant': "",
            'quant_minima': "",
        }
        help_texts = {
            'nome': "Nome",
            'preco': "Preço",
            'quant': "Quantidade",
            'quant_minima': "Quantidade Mínima"
        }


class VendaModelForm(forms.ModelForm):
    def registrar(self, user):
        v = self.save(commit=False)
        v.user = user
        v.produto.quant -= v.quant
        v.save()
        v.produto.save()
        return v.id

    class Meta:
        model = Venda
        fields = ['produto', 'quant', 'desconto', 'cliente']
        labels = {
            'produto': "",
            'desconto': "",
            'quant': "",
            'cliente': "",
        }
        help_texts = {
            'produto': "Produto",
            'desconto': "Desconto",
            'quant': "Quantidade",
            'cliente': "Cliente",
        }

    def __init__(self, user, *args, **kwargs):
        super(VendaModelForm, self).__init__(*args, **kwargs)
        self.fields['produto'].queryset = Produto.objects.filter(user=user)

class MaterialModelForm(forms.ModelForm):
    def material(self, user):
        m = self.save(commit=False)
        m.user = user
        m.save()
        return m.id_material

    class Meta:
        model = Materiais
        fields = ['id_material','nm_material', 'unidade', 'preco_compra', 'tipo', 'validade_ca', 'localizacao', 'currency']
        labels = {
            'nm_material': "",
            'unidade': "",
            'preco_compra': "",
            'tipo': "",
            'validade_ca': "",
            'localizacao': "",
            'currency': "",
            'price_net': "",
        }
        help_texts = {
            'nm_material': "Nome Produto",
            'unidade': "Quantidade",
            'preco_compra': "Preço de Compra",
            'tipo': "Tipo de material comprado",
            'validade_ca': "Data de Compra",
            'localizacao': "local de Compra",
            'currency': "Tipo de Pagamento",
        }

        def __init__(self, user, *args, **kwargs):
            MaterialModelForm = kwargs.material('MaterialModelForm')
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.fields['nm_material'].queryset = MaterialModelForm.objects.filter(user=user)




class BuscarModelForm(forms.Form):
    nome = ModeloCharField('Nome do Produto', 50)

    def get_produto_json(self):
        return get_produto_json(self.cleaned_data['nome'])

    def get_produtos(self, user_creator):
        produtos = get_produtos_produto(self.cleaned_data['nome'], user_creator)
        return produtos
