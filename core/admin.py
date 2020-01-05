from django.contrib import admin
from .models import (
    Marca, 
    Veiculo, 
    Pessoa, 
    Parametros, 
    MovRotativo,
    Mensalista,
    MovMensalista
)

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'checkin', 'checkout', 'valor_hora', 'veiculo', 
        'pago', 'total', 'horas_total')
    #def veiculo(self, obj):
        #return obj.veiculo  #não entendi pq ele inseriu este 'def', acho que nem precisava (aula 170)


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pgto', 'total')


admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)

