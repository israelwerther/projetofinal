from django.forms import ModelForm
from .models import Pessoa, Veiculo, MovRotativo


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class MovRotativoForm(ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__'