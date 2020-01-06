from django.shortcuts import render
from .models import Pessoa


def home(request):
    context = {'mensagem': 'Ola mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})