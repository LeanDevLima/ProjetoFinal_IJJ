## Plano de Teste - Projeto Final - Bugou? QA tá ON! 📅 📦

Esse [repositório](https://github.com/LeanDevLima/ProjetoFinal_IJJ) é dedicado ao Projeto Final do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

Clique nas "►" abaixo para visualizar os conteúdos trabalhados no projeto. Para recolher o conteúdo, basta clicar nas "▼" novamente. 😁


**Integrantes da Squad 02:** [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) 👨🏾‍💻 | [Sara Sara J. M da Cruz](https://www.linkedin.com/in/sara-j-m-da-cruz-08ba19282/) 👩🏾‍💻

**Data de Execução dos testes:** 01/10/2023 📅


<details>
<summary> Cenários de Teste | Gherkin 🌟</summary>
<p>

Este plano de teste descreve os testes a serem executados no Sistema de Vendas do Instituto Joga Junto, com foco na perspectiva do usuário. O sistema é composto por uma aplicação frontend construída com React JS, hospedada na AWS Amplify, e utiliza uma estrutura de backend em NodeJS com um banco de dados MySQL versão 8.

## ID: ZBH-0001 - Login 

**Funcionalidade:** Login com cadastro por Google ou Facebook

**Cenário:** Tentativa de cadastro

**Objetivo:** o objetivo é que seja possível o cadastro

1. ******Dado que****** o usuário está na tela de cadastro
2. ***Quando*** o usuário clica em "ou cadastre-se com" e escolhe a opção de cadastro com Google ou Facebook
3. ***Então*** o sistema deve apresentar resultados

Resultado: Ao clicar em "ou cadastre-se com" através da alternativa que a plataforma fornece, de cadastrar com o Google ou com o Facebook, porém, não se obtém resultado	Deveria ser possível cadastrar-se com essas duas alternativas.

## ID: ZBH-0002 - Texto 

**Funcionalidade:** Experiência visual do usuário

**Cenário:** Layout do site

**Objetivo:** Garantir que haja apenas um texto de registro visível.

1. ***Dado que*** o usuário está na página de registro
2. ***Quando*** o usuário visualiza o texto de registro
3. ***Então*** deve haver apenas um texto de registro visível

Resultado: Ao entrar no site é possível reparar um erro, onde visualizamos que há duas formas de novo cadastramento. Deve haver apenas apenas um texto de registro.

## ID: ZBH-0003 - Login incorreto

**Funcionalidade:** Tratamento de tentativa de login com erro

**Cenário:** Tentativa de login com erro de e-mail

**Objetivo:** Permitir o login mesmo que não haja cadastro com o e-mail.

1. ***Dado que*** o usuário está na tela de login
2. ***Quando*** o usuário tenta efetuar o login com um e-mail que não existe na plataforma
3. ***Então*** o sistema deve informar que o e-mail não está cadastrado

Resultado: Ao tentar criar o login, entrando na alternativa de registro, o site informa que já existe usuário com o email apresentado. O site não deve permitir o login sem que haja cadastro com o e-mail.

## ID: ZBH-0004 - Permissão de acesso

**Funcionalidade:** Restrição de acesso à plataforma

**Cenário:** Acesso após várias tentativas de login

**Objetivo:** Permitir o acesso somente após um cadastro bem-sucedido.

1. ***Dado que*** o usuário está na tela de login
2. ***Quando*** o usuário tenta fazer o login várias vezes com credenciais incorretas
3. ***Então*** o sistema não deve permitir o acesso à plataforma

Resultado: Ao apresentar o mesmo login várias vezes, consegue-se abrir a plataforma. O sistema só deve permitir o acesso somente após um cadastro bem-sucedido.

## ID: ZBH-0005 - Preço

**Funcionalidade:** Exibição de preço de produto

**Cenário:** Exibição de preço ao clicar em "Preço"

**Objetivo:** Mostrar o preço do produto cadastrado.

1. ***Dado que*** o usuário está logado na plataforma
2. ***Quando*** o usuário rola a página para baixo e clica em "Preço"
3. ***Então*** o sistema deve exibir apenas o preço do produto cadastrado

Resultado: Ao entrar na plataforma, rola a página para baixo e clica em "Preço". Deveria aparecer somente o preço do produto cadastrado, mas estão aparecendo vários outros preços.

## ID: ZBH-0006 - Imagem no cadastro do Produto

**Funcionalidade:** Exibição da imagem de produto cadastrado

**Cenário:** Exibição da imagem ao cadastrar o produto

**Objetivo:** Garantir que a imagem seja a do produto cadastrado.

1. ***Dado que*** o usuário está cadastrando um produto
2. ***Quando*** o usuário confere se a imagem está correta 
3. ***Então*** o sistema deve permitir a conclusão do cadastro do produto

Resultado: Ao cadastrar o produto a imagem se sobrepôe às informações. A imagem deve permanecer no mesmo lugar e o site deve permitir que o usuário conclua o cadastro do produto.

## ID: ZBH-0007 - Campo de Pesquisa

**Funcionalidade:** Pesquisa de produtos

**Cenário:** Utilizar o campo de pesquisa para buscar um produto

**Objetivo:** Garantir que o produto pesquisado seja exibido em uma página específica

1. ***Dado que*** o usuário está na plataforma
2. ***Quando*** o usuário clica no ícone de pesquisa e digita o nome do produto
3. ***Então*** o sistema deve gerar o resultado correspondente ao produto pesquisado

Resultado: Ao clicar no ícone de pesquisa e digitar o nome do produto, não gera nenhum resultado. Deveria aparecer o produto pesquisado em uma página específica.

## ID: ZBH-0008 - Leitura do Site

**Funcionalidade:** Exibição do site de forma correta

**Cenário:** Exibição de palavras e textos de modo a facilitar a interação do usuário

**Objetivo:** Mostrar todas as palavras e textos corretamente

1. ***Dado que*** o usuário está acessando o site através de um celular
2. ***Quando*** o usuário entra com o login
3. ***Então*** o sistema deve exibir todas as palavras corretamente

Resultado: Com o celular iPhone, que tem o sistema iOS, ao entrar com o login é possível identificar diversas palavras incompletas na plataforma. O site deve mostrar todas as palavras corretamente no sistema operacional iOS.

## ID: ZBH-0009 - Informações de perfil

**Funcionalidade:** Exibição de informações que estão no perfil do usuário

**Cenário:** Clicar no ícone "perfil" do site

**Objetivo:** Permitir o acesso e a possível edição das informações de perfil

1. ***Dado que*** o usuário está cadastrado 
2. ***Quando*** o usuário entra com o login e clica no ícone "perfil" na barra superior da página
3. ***Então*** o sistema deve exibir as informações de perfil e possibilitar editá-las
   
Resultado: Com o celular iPhone, que tem o sistema iOS, ao fazer o login e clicar no ícone "perfil" que aparece na barra superior da página deveria aparecer as informações do perfil, para possibilitar o acesso e a alteração das informações, porém tais informações não aparecem.

## ID: ZBH-0010 - Registro de produto

**Funcionalidade:** Registro de um novo produto

**Cenário:** Usuário cadastrando um produto novo

**Objetivo:** Permitir o registro do produto com sucesso

1. ***Dado que*** o usuário está cadastrando o produto usando um celular 
2. ***Quando*** o usuário entra com o login e clica no ícone "Adicionar" e coloca as informações
3. ***Então*** o sistema deve permitir o registro do produto na plataforma

Resultado: Com o celular com sistema operacional iOS, ao entrar com o login e clicar no ícone "Adicionar" e inserir as informações. Deveria ser possível registrar o produto na plataforma com sucesso. Porém o site não segue com o cadastro.

## ID: ZBH-0011 - Contato

**Funcionalidade:** Botão de contato com suporte

**Cenário:** Tentativa de contato com suporte

**Objetivo:** Direcionar para um chat onde seja possível a comunicação com a central de atendimento ou suporte técnico

1. ***Dado que*** o usuário está logado na plataforma
2. ***Quando*** o usuário clica no ícone "contato" na barra superior da página
3. ***Então*** o sistema deve direcionar para a central de atendimento
   
Resultado: Ao tentar entrar em contato, clicando no ícone "contato" na barra superior da página, o site nos direciona para um GitHub que não corresponde à area onde obterá ajuda. O sistema deve direcionar para um chat onde seja possível a comunicação com o time responsável em auxiliar o usuário.

## ID: ZBH-0012 - Filtragem de Produtos

**Funcionalidade:** Filtragem de produtos de acordo com a categoria

**Cenário:** Tentativa de visualizar cada produto com sua respectiva categoria

**Objetivo:** Apresentar os produtos de acordo com suas categorias para aprimorar a interação do usuário com os itens cadastrados.

1. ***Dado que*** o usuário está logado na plataforma.
2. ***Quando*** o usuário clica nos ícones correspondentes às categorias "Todos", "Roupas", "Calçados" e "Acessórios".
3. ***Então*** o sistema deve exibir os produtos de acordo com a categoria solicitada.

Resultado: A parte correspondente à categoria "Roupas" está correta. No entanto, nas categorias "Calçados" e "Acessórios", os produtos cadastrados correspondentes não são exibidos.

## ID: ZBH-0013 - Verificação de informação

**Funcionalidade:** Mostrar as informações do produto cadastrado 
**Cenário:** Na intenção de saber todas as informações fornecidas do produto

**Objetivo:** Mostrar todas as informações do produto que forem postas na hora do cadastro do produto 

1. ***Dado que*** o usuário está logado na plataforma.
2. ***Quando*** o usuário busca pela informação fornecidas.
3. ***Então*** o sistema deve exibir as informações correspondentes ao produto.
   
Resultado: A informação de frete não aparece na apresentação do produto.

</details>

<details>
<summary> Report Bugs | Criticidade | Evidências 🌟</summary>
<p>

Esse é o arquivo onde inserimos os bugs incluindo seu nível de criticidade.

O arquivo correspondente está nesse mesmo repositório na pasta \Evidencias.

<img src="Evidencias\Report Bugs - Projeto Final_page-0001.jpg">

</details>

<details>
<summary> Testes automatizados 🌟</summary>
<p>

A parte correspondente a automação de testes nossa squad decidiou dividir em três etapas de acordo com o que foi aprendido durante todo o curso, ressalto que o caso de teste escolhido para os dois primeiros casos abaixo foi o de número 12.

## ID: ZBH-0012 - Filtragem de Produtos

**Funcionalidade:** Filtragem de produtos de acordo com a categoria

**Cenário:** Tentativa de visualizar cada produto com sua respectiva categoria

**Objetivo:** Apresentar os produtos de acordo com suas categorias para aprimorar a interação do usuário com os itens cadastrados.

1. ***Dado que*** o usuário está logado na plataforma.
2. ***Quando*** o usuário clica nos ícones correspondentes às categorias "Todos", "Roupas", "Calçados" e "Acessórios".
3. ***Então*** o sistema deve exibir os produtos de acordo com a categoria solicitada.

Resultado: A parte correspondente à categoria "Roupas" está correta. No entanto, nas categorias "Calçados" e "Acessórios", os produtos cadastrados correspondentes não são exibidos.


<details>
<summary> Testes automatizados I | Programação Estruturada 🌟</summary>

Nessa abordagem fizemos uma automação com um estilo de programação estruturada:

```python
## ID: ZBH-0012 - Filtrar por produto

import sys
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

sys.path.append("projetols")

navegador = Firefox()
navegador.get("https://projetofinal.jogajuntoinstituto.org/")

sleep(2)

campo_email = navegador.find_element(By.NAME, "email")
campo_email.send_keys("leanderson.devlima@gmail.com")

campo_senha = navegador.find_element(By.NAME, "password")
campo_senha.send_keys("jcjcjc@33")

sleep(2)

botao = navegador.find_element(By.XPATH, '//*[@id="root"]/main/form/button')
botao.click()

sleep(2)

def green(message):
    print("\033[92m" + message + "\033[0m")

def red(message):
    print("\033[91m" + message + "\033[0m")

def check_category_success(navegador, link_xpath, item_name):
    try:
        link = navegador.find_element(By.XPATH, link_xpath)
        link.click()
        sleep(2)
        if item_name in navegador.page_source:
            green(f"\nO acesso à categoria '{item_name}' foi bem-sucedido!")
        else:
            raise NoSuchElementException()
    except NoSuchElementException:
        red(f"\nO acesso à categoria '{item_name}' não foi bem-sucedido! (Categoria não encontrada)")

def check_item_in_category(navegador, link_xpath, item_name, category_name):
    try:
        link = navegador.find_element(By.XPATH, link_xpath)
        link.click()
        sleep(3)
        if item_name in navegador.page_source:
            green(f"-► Item '{item_name}' encontrado na categoria '{category_name}'")
        else:
            raise NoSuchElementException()
    except NoSuchElementException:
        red(f"-► Item '{item_name}' não encontrado na categoria '{category_name}'")

check_category_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[1]/li', "Todos")

check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div[3]/div[1]/img', "roupateste", "Todos")
check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div[4]/div[1]/img', "Cal", "Todos")
check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div[5]/div[1]/img', "Oculos SP", "Todos")
check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div[6]/div[1]/img', "Miçanga BA", "Todos")

check_category_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[2]/li', "Roupas")

check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div/div[1]/img', "roupateste", "Roupas")

check_category_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[3]/li', "Calçados")

check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div/div[1]/img', "Cal", "Calçados")

check_category_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[4]/li', "Acessórios")

check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div/div[1]/img', "Oculos SP", "Acessórios")

check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div/div[2]/img', "Miçanga BA", "Acessórios")

check_category_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[5]/li', "Elemento Inexistente")

check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div[7]/div[1]/img', "Acesorio3(nao existe)", "Todos")

sleep(2)
navegador.quit()

```

Detalhes desse código e seus resultados estão na próxima etapa dos testes automatizados e o arquivo correspondente está nesse repositório no caminho Automacao\automacao.py.

</details>



<details>
<summary> Testes automatizados II | Programação Orientada a Objetos 🌟</summary>

Nessa abordagem usamos um estilo de programação Orientado a Objetos onde cada fução foi dividida em arquivos diferentes:

```python

def green(message):
    print("\033[92m" + message + "\033[0m")

def red(message):
    print("\033[91m" + message + "\033[0m")

```
Essa função que está em Automacao\terminal.py tem o propósito de pintar no temrinal de verde e de vermelho, sendo intuitivamente verde para um caso de sucesso e vermelho em caso de falha ou bug.

```python
from selenium.webdriver.common.by import By

def login(navegador, email, senha):
    campo_email = navegador.find_element(By.NAME, "email")
    campo_email.send_keys(email)

    campo_senha = navegador.find_element(By.NAME, "password")
    campo_senha.send_keys(senha)
```
Essa função tem o propósito inserir o email e a senha nos campos corretos da nossa aplicação alvo. O arquivo correspondente está em Automacao\login.py.

```python
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from terminal import green, red

def check_category_success(navegador, link_xpath, item_name):
    try:
        link = navegador.find_element(By.XPATH, link_xpath)
        link.click()
        sleep(2)
        if item_name in navegador.page_source:
            green(f"\nO acesso à categoria '{item_name}' foi bem-sucedido!")
        else:
            raise NoSuchElementException()
    except NoSuchElementException:
        red(f"\nO acesso à categoria '{item_name}' não foi bem-sucedido! (Categoria não encontrada)")        

```

Essa função tem o propósito de encontrar a categoria e informar no console em caso de sucesso. O laço de repetição escolhido foi o ***'try'*** ***'except'*** pois em caso de falha ao encontrar a categoria o código iria exibir um erro de ***'NoSuchElementException'***, o que iria interromper a execução do mesmo. Porém o ***'raise'*** que está dentro de ***'else'*** obriga o código a executar o comando que está em ***'except'***. Exibindo no terminal a informação referente a uma operação malsucedida. O arquivo que se refere a essa função está em Automacao\check_category.py.


```python
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from terminal import green, red

def check_item_in_category(navegador, link_xpath, item_name, category_name):
    try:
        link = navegador.find_element(By.XPATH, link_xpath)
        link.click()
        sleep(3)
        if item_name in navegador.page_source:
            green(f"-► Item '{item_name}' encontrado na categoria '{category_name}'")
        else:
            raise NoSuchElementException()
    except NoSuchElementException:
        red(f"-► Item '{item_name}' não encontrado na categoria '{category_name}'")

```

A mesma lógica da função ***'check_category_success'*** foi usada para a função ***'check_item_in_category'***. O arquivo correspondente está em Automacao\check_item.py.


```python
## ID: ZBH-0012 - Filtrar por produto

import sys
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from check_category import check_category_success
from check_item import check_item_in_category
from login import login

sys.path.append("projetols")

navegador = Firefox()
navegador.get("https://projetofinal.jogajuntoinstituto.org/")

sleep(1)

login(navegador, "leanderson.devlima@gmail.com", "jcjcjc@33")

sleep(1)

botao = navegador.find_element(By.XPATH, '//*[@id="root"]/main/form/button')
botao.click()

sleep(1)

check_category_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[1]/li', "Todos")

check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div[3]/div[1]/img', "roupateste", "Todos")
check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div[4]/div[1]/img', "Cal", "Todos")
check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div[5]/div[1]/img', "Oculos SP", "Todos")
check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div[6]/div[1]/img', "Miçanga BA", "Todos")

check_category_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[2]/li', "Roupas")

check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div/div[1]/img', "roupateste", "Roupas")

check_category_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[3]/li', "Calçados")

check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div/div[1]/img', "Cal", "Calçados")

check_category_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[4]/li', "Acessórios")

check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div/div[1]/img', "Oculos SP", "Acessórios")

check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div/div[2]/img', "Miçanga BA", "Acessórios")

check_category_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[5]/li', "Elemento Inexistente")

check_item_in_category(navegador, '/html/body/div/header/section[2]/div/div/div/div[7]/div[1]/img', "Acesorio3(nao existe)", "Todos")

sleep(3)
navegador.quit()

```
Por fim temos o arquivo Automacao\main.py onde ele importa todas essas funções e passas os argumentos solicitados por elas para que possam ser executadas.

Resultado no terminal:

<img src="Evidencias\resultado_terminal.png">


</details>

<details>
<summary> Testes automatizados III | Biblioteca Behave 🌟</summary>

## ID: ZBH-0001 - Login 

Automação utilizando a biblioteca [Behave](https://behave.readthedocs.io/en/latest/).

Para realização dessa parte da atividade nossa squad usou o cenário de testes ZBH-0001 - Login.

Estrutura:

<img src="Evidencias\estrutura.png">

```feature
Feature: Acessar categorias de produtos

  @testeLogin
  Scenario: Fazer login
    Given o usuário está na página inicial
    When o usuário insere os dados para login, email e senha
    And o usuário clica no botão Iniciar sessão
    Then o sistema permite o login e fecha o navegador
```

No código:

```python
from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

@given("o usuário está na página inicial")
def step_given_acessar_pagina_inicial(context):
    context.navegador = Firefox()
    context.navegador.get("https://projetofinal.jogajuntoinstituto.org/")

@when("o usuário insere os dados para login, email e senha")
def step_when_fazer_login(context):
    context.email = "leanderson.devlima@gmail.com"
    context.senha = "jcjcjc@33"

    campo_email = context.navegador.find_element(By.NAME, "email")
    campo_senha = context.navegador.find_element(By.NAME, "password")
    
    campo_email.send_keys(context.email)
    campo_senha.send_keys(context.senha)

@when("o usuário clica no botão Iniciar sessão")
def step_button_click(context):
    botao = context.navegador.find_element(By.XPATH, '//*[@id="root"]/main/form/button')
    botao.click()
    sleep(3)

@then('o sistema permite o login e fecha o navegador')
def login_success(context):
    expected_url = "https://projetofinal.jogajuntoinstituto.org/products"
    current_url = context.navegador.current_url
    
    assert current_url == expected_url, "URL incorreta após o login. O login falhou."
    
    context.navegador.quit()

```
O propósito desse último teste, conforme foi explicado e demonstrado durante a apresentação, foi executar um login com sucesso e fechar o navegador em seguida.

A execução dessa parte do trabalho mostrou que temos que criar mais intimidade com essa estrutura de execução de testes e com a biblioteca behave, porém com esforço, dedicação e trabalho em equipe, conseguimos finalizar a parte de automação com sucesso.

</details>
</details>

<details>
<summary> Testes de API 🌟</summary>
<p>

Estrutura da API foi montada manualmente de acordo com o swagger, pois não foi possível importar a mesma.

<img src="Evidencias\estruturaAPI.png">

Foi definida uma variável para que não precisasse inserir a mesma URL em cada requisição.

<img src="Evidencias\variavelAPI.png">

O primeiro método GET serviu para verificar se a API estava em funcionamento.
O que durante a apresentação foi demonstrado com sucesso.

<img src="Evidencias\getAPI.png">

Em seguida o POST faz o registro de um usuário.

<img src="Evidencias\usuarioAPI.png">

O próximo POST faz o login desse mesmo usuário gerando um token. O que nos leva para o próximo GET onde o token dinamico



```javascript
pm.sendRequest({
    url: 'http://apipf.jogajuntoinstituto.org/login',
    method: 'POST',
    header: {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: {
        mode: 'raw',
        raw: JSON.stringify({
            "email": "leanderson.devlima@gmail.com",
            "password": "jcjcjc@33"
        })
    }
}, function (err, res) {
    pm.environment.set('tokenJogaJunto', res.json().token);
});
```

