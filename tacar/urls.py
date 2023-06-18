
from django.contrib import admin
from django.urls import path, include
from core.views import apresentacao, login, cadastro_contaBancaria, cadastro_cartao, home, editar_perfil, grafico_gastos, relatorios, conta_bancaria, pagamentos, perfil, realizando_pagamento, cadastro_despesa, remover_contaBancaria
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', apresentacao, name='url_tela_inicial'),
    path('cadastro/', cadastro_contaBancaria, name='cadastro'),
    path('login/', login, name='url_login'),
    path('cadastro_cartao/', cadastro_cartao, name='url_cadastro_cartao'),
    path('home/', home, name='url_home'),
    path('grafico_gastos/', grafico_gastos, name='url_grafico_gastos'),
    path('relatorios/', relatorios, name='url_relatorios'),
    path('conta_bancaria/', conta_bancaria, name='url_conta_bancaria'),
    path('pagamentos/', pagamentos, name='url_pagamentos'),
    path('perfil/<str:pessoa>/', perfil, name='url_perfil'),
    path('editar_perfil/<int:id>/', editar_perfil, name='url_editar_perfil'),
    path('realizando_pagamento/<int:id>/', realizando_pagamento, name='realizando_pagamento'),
    path('cadastro_despesa/', cadastro_despesa, name='cadastro_despesa'),
    path('conta/remover/<int:id_conta>/', remover_contaBancaria, name='remover_conta'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
