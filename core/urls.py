from django.urls import path, include
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalista,
    pessoa_novo,
    veiculo_novo,
    movrotativos_novo,
    mensalista_novo
)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa-novo/', pessoa_novo, name='core_pessoa_novo'),
    path('veiculo-novo/', veiculo_novo, name='core_veiculo_novo'),
    path('mov-rot-novo/', movrotativos_novo, name='core_movrotativos_novo'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista_novo'),
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('mov-mensal/', lista_movmensalista, name='core_lista_movmensalista'),
]
    