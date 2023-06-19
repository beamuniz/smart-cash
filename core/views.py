
from django.shortcuts import get_object_or_404, render, redirect
from core.models import FormaPagamento, Usuario, Cartao, Despesas, Relatorio, ContaBancaria, Notificacao
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from core.forms import FormContaBancaria, FormCartao, FormUsuario, FormDespesas
from django.contrib.auth import authenticate, login

# Create your views here.

def apresentacao(request):
    return render(request,'core/apresentacao.html')

class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('url_principal')
    template_name = 'registration/registrar.html'

def cadastro_contaBancaria(request):
    form = FormContaBancaria(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_cadastro_cartao')
    contexto = {'form': form, 'bancaria': 'Cadastro com sua conta bancária', 'formulario':True}
    return render(request, 'cadastro.html', contexto)

def cadastro_cartao(request):
    form = FormCartao(request.POST or None, request.FILES or None)
    if form.is_valid():
            form.save()
            return redirect('url_login')
    contexto = {'form': form, 'cartao': 'Cadastre seu cartão', 'formulario':False}
    return render(request, 'core/cadastro_cartao.html', contexto)

def login(request):
    if request.method == 'POST':
        conta = request.POST['conta']
        senha = request.POST['senha']
        try:
            pagamentos = Despesas.objects.all()
            user = Usuario.objects.get(conta=conta, senha=senha)
            context = {'pessoa': user, 'pagamentos': pagamentos}
            if conta == user.conta and senha == user.senha:
                request.session['usuario_nome'] = user.nome
                request.session['usuario_id'] = user.contaBancaria.id_contaBancaria
                return render(request, 'core/home.html', context)  # redirect('url_home', context)
        except Usuario.DoesNotExist:
            error_message = 'Número da conta ou senha inválidos.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def perfil(request, id):  
    try:
        user = Usuario.objects.get(id=id)
        contexto = {'dados': user}
        return  render(request, 'core/perfil.html', contexto)
    except ContaBancaria.DoesNotExist:
        error_message = 'Usuário não encontrado.'
        return render(request, 'core/mensagem.html', {'error_message': error_message})

def editar_perfil(request, id):
    user = Usuario.objects.get(id=id)
    if request.method == 'POST':
        form = FormUsuario(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('url_perfil', id=user.contaBancaria.id_contaBancaria)  # Redirecionar para a página de perfil atualizada
    else:
        form = FormUsuario(instance=user)
    
    contexto = {'form': form}
    return render(request, 'core/editar_perfil.html', contexto)

def conta_bancaria(request, id_contaBancaria):
    try:
        user = ContaBancaria.objects.get(id_contaBancaria=id_contaBancaria)
        contexto = {'dados': user}
        return  render(request, 'core/conta_bancaria.html', contexto)
    except ContaBancaria.DoesNotExist:
        error_message = 'Usuário não encontrado.'
        return render(request, 'core/mensagem.html', {'error_message': error_message})


def pagamentos(request):
    pagamentos = Despesas.objects.all()
    contexto = {'pagamentos': pagamentos}
    return render(request, 'core/pagamentos.html', contexto)

def logout_view(request):
    return render(request, 'core/apresentacao.html')

def home(request): 
    user = Usuario.objects.all()
    context = {'pessoa': user}
    return render(request, 'core/home.html', context)

def graficos_gastos(request):
    return render(request, 'core/graficos_gastos.html')

def relatorios(request):
        dados = Relatorio.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/relatorios.html', contexto)

def cadastro_despesa(request, id_contaBancaria):
    form = FormDespesas(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return render(request, 'core/pagamentos.html')
    contexto = {'form': form}
    return render(request, 'core/cadastro_despesa.html', contexto)

def realizando_pagamento(request, id):
        despesa = get_object_or_404(Despesas, id=id)
        despesa.status = True
        despesa.save()
        contexto = {'dados': despesa}
        return render(request, 'core/realizando_pagamento.html', contexto)


def pagamento_realizado(request, id):
        despesa = Despesas.objects.get(id=id) 
        despesa.status = True
        contexto = {'dados': despesa}
        return render(request, 'core/pagamento_realizado.html', contexto)

def remover_contaBancaria(request, pessoa):
    if request.method == 'POST':
        conta = ContaBancaria.objects.get(proprietario=pessoa)
        conta.delete()
        return redirect('url_login')

def confirmar_remocao_conta(request, pessoa):
    obj = ContaBancaria.objects.get(proprietario=pessoa)

    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Conta excluída com sucesso')
        return render(request, 'core/home.html')
    
    return render(request, 'core/confirma_remocao_exclusao.html', {'dados': obj})
