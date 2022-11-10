
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages 
from usuarios.models import User
from clientes.models import Cad_Cliente, Info_cliente
from clientes.forms import ClienteForm, Info_clienteForm
from tablib import Dataset
from .resources import Cad_ClienteResource, Info_clienteResource
from django.shortcuts import get_object_or_404
from django.core import serializers


def index(request):
    return render(request,'clientes/index.html')

def cadastrar_clientes_view(request):
    form = ClienteForm(request.user)

    if request.method == 'POST':
        form = ClienteForm(request.user, request.POST)

        if form.is_valid():
            prestador = form.save(commit=False)
            prestador.user = request.user
            prestador.save()
            return index(request)
        else:
            print('ERROR FORM')

    return render(request, 'clientes/clientes.html',{'form': form})

def nome_clientes_view(request):
    form = Info_clienteForm(request.user)

    if request.method == 'POST':
        form = Info_clienteForm(request.user, request.POST)

        if form.is_valid():
            prestador = form.save(commit=False)
            prestador.user = request.user
            prestador.save()
            return index(request)
        else:
            print('ERROR FORM')

    return render(request, 'clientes/nome_clientes.html',{'form': form})   

def cadastros_list(request):
    cliente = request.user
    cadastros = Info_cliente.objects.filter(user=usuario.id).order_by('-criacao')
    return render(request,'cadastros_lista.html',{
        'cadastros':cadastros
    })

def cadastro_enviado(request,pk):
    cadastros=get_object_or_404(Info_cliente,pk=pk)
    data = serializers.serialize("python", Info_cliente.objects.filter(pk=pk))
    return render(request,'cadastro_detalhe.html',{'cadastros':cadastros,'data':data})

def cadastros_clientes_list(request):
    usuario = request.user
    cadastrospac = Info_cliente.objects.filter(usuario=usuario.id).order_by('-date_add')
    return render(request,'cadastros_clientes_lista.html',{
        'cadastrospac':cadastrospac
    })

def cadastro_clientes_enviado(request,pk):
    cadastrospac=get_object_or_404(Info_cliente,pk=pk)
    data = serializers.serialize("python", Info_cliente.objects.filter(pk=pk))
    return render(request,'cadastro_clientes_detalhe.html',{'cadastrospac':cadastrospac,'data':data})    



def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        Info_clienteResource = Info_clienteResource()
        dataset = Info_clienteResource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   

    return render(request, 'clientes/export.html')    