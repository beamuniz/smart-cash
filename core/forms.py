from core.models import Cartao, ContaBancaria, Despesas, FormaPagamento, Notificacao, Relatorio, Usuario
from django.forms import ModelForm
from captcha.fields import CaptchaField


class FormUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = 'nome', 'foto'


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

class FormDespesas(ModelForm):
    class Meta:
        model = Despesas
        fields = 'nome', 'valor', 'categoria', 'dataPagamento', 'dataVencimento', 'pagamento'

class Notificacao(ModelForm):
    class Meta:
        model = Notificacao
        fields = '__all__'

class FormaPagamento(ModelForm):
    class Meta:
        model = FormaPagamento
        fields = '__all__'
