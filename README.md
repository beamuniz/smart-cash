# Smart Cash

<div align="center">

 <img src="static_files/symbol.png" alt="smart cash" style="width: 200px; height: auto;">

</div>

## Descrição do Projeto
O Smart Cash é um aplicativo de banco e débito automático desenvolvido com o framework Django. Ele permite que os usuários cadastrem suas contas bancárias, cartões de crédito, realizem login, visualizem informações pessoais, editem seus perfis, realizem pagamentos, acessem relatórios financeiros e muito mais.

## Requerimentos
- asgiref==3.6.0
- beautifulsoup4==4.12.2
- crispy-bootstrap4==2022.1
- dj-database-url==2.0.0
- dj-static==0.0.6
- Django
- django-bootstrap-datepicker-plus==5.0.3
- django-bootstrap4==23.1
- django-crispy-forms==2.0
- django-environ==0.10.0
- django-ranged-response==0.2.0
- django-simple-captcha==0.5.17
- form==0.0.1
- gunicorn==20.1.0
- path==16.6.0
- Pillow==9.4.0
- psycopg2==2.9.6
- pydantic==1.10.9
- soupsieve==2.4.1
- sqlparse==0.4.3
- static3==0.7.0
- typing_extensions==4.6.3
- tzdata==2022.7

## Instalação
1. Certifique-se de ter o Python e o pip instalados em seu ambiente de desenvolvimento.
2. Clone o repositório do Smart Cash para o seu ambiente local.
3. Navegue até o diretório raiz do projeto.
4. Execute o seguinte comando para instalar as dependências necessárias:

`pip install -r requirements.txt`

5. Após a instalação das dependências, execute o seguinte comando para iniciar o servidor de desenvolvimento:

`python manage.py runserver`

6. Acesse o aplicativo em seu navegador usando o seguinte URL: [http://localhost:8000/](http://localhost:8000/)

## Uso
- **Apresentação:** Página inicial do aplicativo.
- **Registrar:** Permite que os usuários se registrem no aplicativo.
- **Cadastro de Conta Bancária:** Permite que os usuários cadastrem suas contas bancárias.
- **Cadastro de Cartão:** Permite que os usuários cadastrem seus cartões de crédito.
- **Login:** Permite que os usuários façam login no aplicativo.
- **Perfil:** Exibe informações pessoais do usuário.
- **Editar Perfil:** Permite que os usuários editem suas informações pessoais.
- **Conta Bancária:** Exibe informações detalhadas da conta bancária do usuário.
- **Pagamentos:** Exibe uma lista de pagamentos realizados.
- **Logout:** Faz o logout do usuário e redireciona para a página de apresentação.
- **Home:** Página inicial do usuário após o login.
- **Gráficos de Gastos:** Exibe gráficos e estatísticas de gastos.
- **Relatórios:** Exibe relatórios financeiros.
- **Cadastro de Despesa:** Permite que os usuários cadastrem suas despesas.
- **Realizando Pagamento:** Exibe uma página de confirmação antes de realizar um pagamento.
- **Pagamento Realizado:** Confirmação de que o pagamento foi realizado com sucesso.
- **Remover Conta Bancária:** Permite que os usuários removam suas contas bancárias.

## Contribuição
1. Faça o fork do repositório do Smart Cash.
2. Crie uma nova branch com sua contribuição:

`git checkout -b minha-contribuicao`

3. Faça as alterações desejadas e adicione commits significativos.
4. Envie sua branch com as alterações para o repositório remoto:

`git push origin minha-contribuicao`

5. Abra um pull request no repositório original e aguarde a revisão e a aprovação da sua contribuição.

Este projeto foi desenvolvido como parte do projeto final das disciplinas Análise Orientada a Objetos e Linguagem de Programação III do curso de Análise e Desenvolvimento de Sistemas.
