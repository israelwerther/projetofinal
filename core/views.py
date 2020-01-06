from django.shortcuts import render
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo,
)


def home(request):
    context = {'mensagem': 'Ola mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    return render(
        request, 'core/lista_movrotativos.html', {'mov_rot': mov_rot})
        