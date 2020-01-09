from django.shortcuts import render, redirect
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo,
    Mensalista,
    MovMensalista    
)

from .forms import PessoaForm, VeiculoForm, MovRotativoForm

def home(request):
    context = {'mensagem': 'Ola mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')
    

def lista_veiculos(request):
    form = VeiculoForm()
    veiculos = Veiculo.objects.all()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'form': form, 'mov_rot': mov_rot}
    return render(
        request, 'core/lista_movrotativos.html', data)


def movrotativos_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(
        request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas})


def lista_movmensalista(request):
    mov_mensalistas = MovMensalista.objects.all()
    return render(
        request, 'core/lista_movmensalistas.html', {'mov_mensalistas': mov_mensalistas})
        