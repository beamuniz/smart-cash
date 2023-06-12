from django.contrib import admin
from core.models import Cartao, ContaBancaria, Despesas, FormaPagamento, Notificacao, Usuario, Relatorio



# Register your models here.
admin.site.register(Cartao)
admin.site.register(ContaBancaria)
admin.site.register(Despesas)
admin.site.register(FormaPagamento)
admin.site.register(Notificacao)
admin.site.register(Usuario)
admin.site.register(Relatorio)