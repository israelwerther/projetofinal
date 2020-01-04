from django.db import models


class Pessoa(models.Model):
    nome         = models.CharField(max_length=100)
    endereco     = models.CharField(max_length=200)
    telefone     = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome         = models.CharField(max_length=50)

    def __str__(self):
        return self.nome    


class Veiculo(models.Model):
    marca        = models.ForeignKey(Marca, on_delete=models.PROTECT)
    placa        = models.CharField(max_length=7)
    proprietario = models.ForeignKey(Pessoa, on_delete=models.PROTECT, blank=True, null=True) #Apenas para não precisar preencher na hora, mas depois verificar qual a necessidade disto >> blank=True,null=True,
    cor          = models.CharField(max_length=15)
    observacoes  = models.TextField()

    def __str__(self):
        return self.marca.nome + ' - ' + self.placa

#como alternativa crie uma classe bairro também com uma foreignkey