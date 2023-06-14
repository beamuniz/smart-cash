"""tacar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import apresentacao, login, cadastro, cartao, login_validation
from django.conf.urls.static import static
from django.conf import settings
""" from core.views import home, cadastro_cliente, listagem_cliente, cadastro_veiculo, cadastro_fabricante, listagem_veiculo,\
    listagem_fabricante, Registrar, atualiza_cliente, atualiza_veiculo, atualiza_fabricante, exclui_cliente, exclui_veiculo, exclui_fabricante, \
    cadastro_tabelaPreco, listagem_tabelaPreco, atualiza_tabelaPreco, exclui_tabelaPreco, cadastro_rotativo, listagem_rotativo, cadastro_mensalista, \
    listagem_mensalista, atualiza_mensalista, exclui_mensalista,atualiza_rotativo, exclui_rotativo """



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', apresentacao, name='Tela Inicial'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='Login'),
    path('cadastro-cartao/', cartao, name='cadastro_cartao'),
    path('home/', login_validation, name='login_validation')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
