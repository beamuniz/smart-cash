from django.db import models
import math
# Create your models here.

class Cartao(models.Model):
    nomeTitular = models.CharField(max_length=100, verbose_name='Nome do Titular')
    numeroCartao = models.CharField(max_length=30, verbose_name='Número do Cartão')
    validade = models.DateTimeField(auto_now=False, verbose_name='Validade')
    cvv = models.IntegerField(verbose_name='CVV')
    class Meta:
        verbose_name_plural='Cartões'
    def __str__(self):
        return f"{self.numeroCartao} ({self.nomeTitular})"
    

class ContaBancaria(models.Model):
    proprietario = models.CharField(max_length=45, verbose_name='Proprietário')
    agencia = models.IntegerField(verbose_name='Agência')
    conta = models.CharField(max_length=100, verbose_name='Número da Conta')
    cartao = models.ForeignKey('Cartao', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Cartão')
    senha = models.CharField(max_length=100, verbose_name='Senha', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Contas Bancárias'

    def save(self, *args, **kwargs):
        created = False
        if not self.pk:
            created = True

        super().save(*args, **kwargs)

        if created:
            usuario, created = Usuario.objects.get_or_create(contaBancaria=self)
        
        usuario.nome = self.proprietario
        usuario.senha = self.senha
        usuario.conta = self.conta
        usuario.save()

    def __str__(self):
        return f"{self.conta}, {self.proprietario}"

class FormaPagamento(models.Model):
    tipo = models.CharField(max_length=45, null=True, blank=True, verbose_name='Nome')
    class Meta:
        verbose_name_plural = 'FormasDePagamentos'  

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45, null=True, blank=True, verbose_name='Nome')
    foto = models.ImageField(upload_to='foto_cliente',blank=True, null=True, verbose_name='Foto')
    senha = models.CharField(max_length=100, verbose_name='Senha')
    conta = models.CharField(max_length=100, null=True, blank=True, verbose_name='Número da Conta')
    contaBancaria = models.ForeignKey(ContaBancaria, on_delete = models.CASCADE, blank=True, null=True, verbose_name='Número da Conta')
    class Meta:
        verbose_name_plural='Usuários'

    def __str__(self):
        return self.nome if self.nome else str(self.id_usuario)

class Notificacao(models.Model):
    mensagem = models.CharField(max_length=100, verbose_name='Mensagem')
    notificacoesAtivas = models.BooleanField(blank=True, null=True, verbose_name='Status')
    data_envio = models.DateTimeField(auto_now=False, verbose_name='Entrada')
    notificacaoPagamento = models.BooleanField(blank=True, null=True, verbose_name='Notificação do Pagamento')
    intervaloNotificacoes = models.IntegerField(blank=True, null=True, verbose_name='Intervalo de Notificações')
    diasAntesVencimento = models.IntegerField(blank=True, null=True, verbose_name='diasAntesVencimento')
    class Meta:
        verbose_name_plural = 'Notificações'
    def __str__(self):
        return f'{self.mensagem}:{self.notificacoesAtivas}'    

class Despesas(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True, verbose_name='Titulo da Despesa')
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    status = models.BooleanField(verbose_name='Status', default=False)
    categoria = models.CharField(max_length=100, verbose_name='Categoria')
    dataPagamento = models.DateField(verbose_name='DataPagamento')
    dataVencimento = models.DateField(verbose_name='DataVencimento')
    pagamento = models.ForeignKey(FormaPagamento, on_delete = models.SET_NULL, blank=True, null=True,verbose_name='FormaPagamento')
    notificacaoDespesas = models.ForeignKey(Notificacao, on_delete = models.SET_NULL, blank=True, null=True,verbose_name='Notificacao')
    class Meta:
        verbose_name_plural = 'Despesas'

    def __str__(self):
        return str(self.nome)

class Relatorio(models.Model):
    nomeItens = models.ForeignKey(Despesas, max_length=100, on_delete=models.CASCADE, verbose_name='Título da conta')
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    geracaoRelatorio = models.DateField(verbose_name='Relatório gerado')
    class Meta:
        verbose_name_plural = 'Relatorios'

    def __str__(self):
        return self.geracaoRelatorio

