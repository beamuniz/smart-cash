
from django.contrib import admin
from django.urls import path, include
from core.views import apresentacao, login, cadastro_contaBancaria, cadastro_cartao, home, editar_perfil, graficos_gastos, relatorios, conta_bancaria, pagamentos, perfil, realizando_pagamento, cadastro_despesa, remover_contaBancaria, pagamento_realizado, confirmar_remocao_conta
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', apresentacao, name='url_tela_inicial'),
    path('cadastro/', cadastro_contaBancaria, name='url_cadastro'),
    path('login/', login, name='url_login'),
    path('cadastro_cartao/', cadastro_cartao, name='url_cadastro_cartao'),
    path('inicial/', home, name='url_home'),
    path('home/', home, name='url_home'),
    path('graficos_gastos/', graficos_gastos, name='url_grafico_gastos'),
    path('relatorios/', relatorios, name='url_relatorios'),
    path('conta_bancaria/<int:id_contaBancaria>/', conta_bancaria, name='url_conta_bancaria'),
    path('pagamentos/', pagamentos, name='url_pagamentos'),
    path('perfil/<int:id>/', perfil, name='url_perfil'),
    path('editar_perfil/<int:id>/', editar_perfil, name='url_editar_perfil'),
    path('realizando_pagamento/<int:id>/', realizando_pagamento, name='url_realizando_pagamento'),
    path('cadastro_despesa/<int:id_contaBancaria>', cadastro_despesa, name='url_cadastro_despesa'),
    path('remocao_conta/<str:pessoa>/', remover_contaBancaria, name='url_remover_conta'),
    path('confirmar_remocao_conta/', confirmar_remocao_conta, name='url_confirmar_remocao_conta'),
    path('pagamento_realizado/<int:id>/', pagamento_realizado, name='url_pagamento_realizado'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
