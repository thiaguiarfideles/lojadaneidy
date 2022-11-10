from django.shortcuts import render, redirect
from django.contrib import messages
from usuarios.models import User

#from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required

from .models import Produto, Imagem, Materiais
from .forms import ProdutoModelForm, VendaModelForm, BuscarModelForm, ImagemModelForm, MaterialModelForm
from .views_func import add_estado, gerar_grafico_mensal, gerar_grafico_anual

from operator import attrgetter
from threading import Thread




@login_required
def index_estoque(request):
    user_creator = request.user
    t_mes = Thread(gerar_grafico_mensal(user_creator))
    t_ano = Thread(gerar_grafico_anual(user_creator))
    t_mes.start()
    t_ano.start()
    context = {
        'url_anual': "images/" + str(user_creator) + "/grafico_anual.png",
        'url_mensal': "images/" + str(user_creator) + "/grafico_mensal.png",
    }
    return render(request, "index_estoque.html", context)


@login_required
def vender(request):
    formvenda = VendaModelForm(request.user, request.POST or None)
    if str(request.method) == "POST":
        if formvenda.is_valid():
            formvenda.registrar(request.user)
            formvenda = VendaModelForm(request.user)
            messages.success(request, "Venda Realizada com Sucesso")

        else:
            messages.error(request, "Venda Não Realizada")
    context = {
        'form': formvenda
    }
    return render(request, "vender.html", context)


@permission_required
def cadastrar(request):
    formproduto = ProdutoModelForm(request.POST or None)
    formimagem = ImagemModelForm(request.FILES or None)

    if str(request.method) == "POST":
        if formproduto.is_valid():
            pk = formproduto.registrar(request.user)
            formproduto = ProdutoModelForm()

            messages.success(request, "Produto cadastrado com sucesso!")

            if formimagem.is_valid():
                imagem = Imagem(imagem=request.FILES['imagem'])
                imagem.titulo = "p_" + str(pk)
                imagem.salvar()
                formimagem = ImagemModelForm()
        else:
            messages.error(request, "Produto não pode ser cadastrado.")
    context = {
        'form': formproduto,
        'formimagem': formimagem,
        'user_id': request.user.id
    }
    return render(request, "cadastrar.html", context)

@permission_required
def material(request):
    formmaterial = MaterialModelForm(request.POST or None)

    if str(request.method) == "POST":
        if formmaterial.is_valid():
            pk = formmaterial.material(request.user)
            formmaterial = MaterialModelForm()

            messages.success(request, "Material cadastrado com sucesso!")

        else:
            messages.error(request, "Material não pode ser cadastrado.")
    context = {
        'form': formmaterial,
        'user_id': request.user.id
    }
    def get_form(self):
        '''add date picker in forms'''
        form = super(material, self).get_form()
        form.fields['validade_ca'].widget = SelectDateWidget()
        return form
    return render(request, "material.html", context)    


@login_required
def listar(request):
    user_creator = request.user
    produtos = list(map(add_estado, Produto.objects.filter(user=user_creator)))
    produtos.sort(key=attrgetter('nome'))
    context = {
        'produtos': produtos
    }
    return render(request, "listar.html", context)


@login_required
def buscar(request):
    user_creator = request.user
    formbusca = BuscarModelForm(request.POST or None)
    produtos = None
    if str(request.method) == "POST":
        if formbusca.is_valid():
            produtos = formbusca.get_produtos(user_creator)
            if produtos:
                formbusca = BuscarModelForm()
                produtos = list(map(add_estado, produtos))
                produtos.sort(key=attrgetter('nome'))
            else:
                messages.error(request, "Produto Não Encontrado")
    context = {
        'form': formbusca,
        'produtos': produtos
    }
    return render(request, "buscar.html", context)


@permission_required
def editar(request, pk):
    produto = Produto.objects.get(id=pk)

    data = produto.to_json()

    formproduto = ProdutoModelForm(data or None)
    formimagem = ImagemModelForm(request.FILES or None)

    if str(request.method) == "POST":
        if formproduto.is_valid() and len(request.POST) == 7:
            produto.nome = request.POST["nome"]
            produto.preco = request.POST["preco"]
            produto.quant = request.POST["quant"]
            produto.quant_minima = request.POST["quant_minima"]

            produto.save()
            formproduto = ProdutoModelForm(data)
            messages.success(request, "Alterações Salvas")

        if formimagem.is_valid():
            imagem = Imagem(imagem=request.FILES['imagem'])
            imagem.titulo = "p_" + str(pk)
            imagem.salvar()
            formimagem = ImagemModelForm()
    context = {
        'formproduto': formproduto,
        'formimagem': formimagem,
        'produto': produto,
    }
    return render(request, "editar.html", context)


@permission_required
def deletar(request, pk):
    Produto.objects.filter(id=pk).delete()
    imagem = Imagem()
    imagem.titulo = pk
    try:
        imagem.remover()
    except FileNotFoundError:
        pass
    messages.info(request, "Produto Excluido")
    return redirect('listar')
