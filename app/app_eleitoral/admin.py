from django.contrib import admin
from .models import Departamento, Pessoa, PedidoPrazo, Processo, Tramitacao, Portaria, EnvioProcesso, Documento, Funcionario

admin.site.register(Departamento)
admin.site.register(Pessoa)
admin.site.register(PedidoPrazo)
admin.site.register(Processo)
admin.site.register(Tramitacao)
admin.site.register(Portaria)
admin.site.register(EnvioProcesso)
admin.site.register(Documento)
admin.site.register(Funcionario)