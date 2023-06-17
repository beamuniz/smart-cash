from core.models import Cartao, ContaBancaria, Despesas, FormaPagamento, Notificacao, Relatorio, Usuario
from django.forms import ModelForm
from captcha.fields import CaptchaField


class Usuario(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Usuario
        fields ='__all__'


class FormContaBancaria(ModelForm):
    class Meta:
        model = ContaBancaria
        fields = 'proprietario', 'agencia', 'conta', 'senha'


class FormCartao(ModelForm):
    class Meta:
        model = Cartao
        fields ='__all__'


class Relatorio(ModelForm):
    class Meta:
        model = Relatorio
        fields ='__all__'

class Despesas(ModelForm):
    class Meta:
        model = Despesas
        fields = '__all__'

class Notificacao(ModelForm):
    class Meta:
        model = Notificacao
        fields = '__all__'

class FormaPagamento(ModelForm):
    class Meta:
        model = FormaPagamento
        fields = '__all__'
