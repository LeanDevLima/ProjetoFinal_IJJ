# ID: ZBH-0001 - Login 

Funcionalidade: Login com cadastro por Google ou Facebook

Cenário: Tentativa de cadastro

Objetivo: o objetivo é que seja possível o cadastro

1. Dado que o usuário está na tela de cadastro
2. Quando o usuário clica em "ou cadastre-se com" e escolhe a opção de cadastro com Google ou Facebook
3. Então o sistema deve apresentar resultados

Resultado: Ao clicar em "ou cadastre-se com" através da alternativa que a plataforma fornece, de cadastrar com o Google ou com o Facebook, porém, não se obtém resultado	Deveria ser possível cadastrar-se com essas duas alternativas.

Evidência:

# ID: ZBH-0002 - Texto 

Funcionalidade: Experiência visual do usuário

Cenário: Layout do site

Objetivo: Garantir que haja apenas um texto de registro visível.

1. Dado que o usuário está na página de registro
2. Quando o usuário visualiza o texto de registro
3. Então deve haver apenas um texto de registro visível

Resultado: Ao entrar no site é possível reparar um erro, onde visualizamos que há duas formas de novo cadastramento. Deve haver apenas apenas um texto de registro.

# ID: ZBH-0003 - Login incorreto

Funcionalidade: Tratamento de tentativa de login com erro

Cenário: Tentativa de login com erro de e-mail

Objetivo: Permitir o login mesmo que não haja cadastro com o e-mail.

1. Dado que o usuário está na tela de login
2. Quando o usuário tenta efetuar o login com um e-mail que não existe na plataforma
3. Então o sistema deve informar que o e-mail não está cadastrado

Resultado: Ao tentar criar o login, entrando na alternativa de registro, o site informa que já existe usuário com o email apresentado. O site não deve permitir o login sem que haja cadastro com o e-mail.

# ID: ZBH-0004 - Permissão de acesso

Funcionalidade: Restrição de acesso à plataforma

Cenário: Acesso após várias tentativas de login

Objetivo: Permitir o acesso somente após um cadastro bem-sucedido.

1. Dado que o usuário está na tela de login
2. Quando o usuário tenta fazer o login várias vezes com credenciais incorretas
3. Então o sistema não deve permitir o acesso à plataforma

Resultado: Ao apresentar o mesmo login várias vezes, consegue-se abrir a plataforma. O sistema só deve permitir o acesso somente após um cadastro bem-sucedido.

# ID: ZBH-0005 - Preço

Funcionalidade: Exibição de preço de produto

Cenário: Exibição de preço ao clicar em "Preço"

Objetivo: Mostrar o preço do produto cadastrado.

1. Dado que o usuário está logado na plataforma
2. Quando o usuário rola a página para baixo e clica em "Preço"
3. Então o sistema deve exibir apenas o preço do produto cadastrado

Resultado: Ao entrar na plataforma, rola a página para baixo e clica em "Preço". Deveria aparecer somente o preço do produto cadastrado, mas estão aparecendo vários outros preços.

# ID: ZBH-0006 - Imagem no cadastro do Produto

Funcionalidade: Exibição da imagem de produto cadastrado

Cenário: Exibição da imagem ao cadastrar o produto

Objetivo: Garantir que a imagem seja a do produto cadastrado.

1. Dado que o usuário está cadastrando um produto
2. Quando o usuário confere se a imagem está correta 
3. Então o sistema deve permitir a conclusão do cadastro do produto

Resultado: Ao cadastrar o produto a imagem se sobrepôe às informações. A imagem deve permanecer no mesmo lugar e o site deve permitir que o usuário conclua o cadastro do produto.

# ID: ZBH-0007 - Campo de Pesquisa

Funcionalidade: Pesquisa de produtos

Cenário: Utilizar o campo de pesquisa para buscar um produto

Objetivo: Garantir que o produto pesquisado seja exibido em uma página específica

1. Dado que o usuário está na plataforma
2. Quando o usuário clica no ícone de pesquisa e digita o nome do produto
3. Então o sistema deve gerar o resultado correspondente ao produto pesquisado

Resultado: Ao clicar no ícone de pesquisa e digitar o nome do produto, não gera nenhum resultado. Deveria aparecer o produto pesquisado em uma página específica.

# ID: ZBH-0008 - Leitura do Site

Funcionalidade: Exibição do site de forma correta

Cenário: Exibição de palavras e textos de modo a facilitar a interação do usuário

Objetivo: Mostrar todas as palavras e textos corretamente

1. Dado que o usuário está acessando o site através de um celular
2. Quando o usuário entra com o login
3. Então o sistema deve exibir todas as palavras corretamente

Resultado: Com o celular iPhone, que tem o sistema iOS, ao entrar com o login é possível identificar diversas palavras incompletas na plataforma. O site deve mostrar todas as palavras corretamente no sistema operacional iOS.

# ID: ZBH-0009 - Informações de perfil

Funcionalidade: Exibição de informações que estão no perfil do usuário

Cenário: Clicar no ícone "perfil" do site

Objetivo: Permitir o acesso e a possível edição das informações de perfil

1. Dado que o usuário está cadastrado 
2. Quando o usuário entra com o login e clica no ícone "perfil" na barra superior da página
3. Então o sistema deve exibir as informações de perfil e possibilitar editá-las
   
Resultado: Com o celular iPhone, que tem o sistema iOS, ao fazer o login e clicar no ícone "perfil" que aparece na barra superior da página deveria aparecer as informações do perfil, para possibilitar o acesso e a alteração das informações, porém tais informações não aparecem.

# ID: ZBH-0010 - Registro de produto

Funcionalidade: Registro de um novo produto

Cenário: Usuário cadastrando um produto novo

Objetivo: Permitir o registro do produto com sucesso

1. Dado que o usuário está cadastrando o produto usando um celular 
2. Quando o usuário entra com o login e clica no ícone "Adicionar" e coloca as informações
3. Então o sistema deve permitir o registro do produto na plataforma

Resultado: Com o celular com sistema operacional iOS, ao entrar com o login e clicar no ícone "Adicionar" e inserir as informações. Deveria ser possível registrar o produto na plataforma com sucesso. Porém o site não segue com o cadastro.

# ID: ZBH-0011 - Contato

Funcionalidade: Botão de contato com suporte

Cenário: Tentativa de contato com suporte

Objetivo: Direcionar para um chat onde seja possível a comunicação com a central de atendimento ou suporte técnico

1. Dado que o usuário está logado na plataforma
2. Quando o usuário clica no ícone "contato" na barra superior da página
3. Então o sistema deve direcionar para a central de atendimento
   
Resultado: Ao tentar entrar em contato, clicando no ícone "contato" na barra superior da página, o site nos direciona para um GitHub que não corresponde à area onde obterá ajuda. O sistema deve direcionar para um chat onde seja possível a comunicação com o time responsável em auxiliar o usuário.


# ID: ZBH-0012 - Filtragem de Produtos

Funcionalidade: Filtragem de produtos de acordo com a categoria

Cenário: Tentativa de visualizar cada produto com sua respectiva categoria

Objetivo: Apresentar os produtos de acordo com suas categorias para aprimorar a interação do usuário com os itens cadastrados.

1. Dado que o usuário está logado na plataforma.
2. Quando o usuário clica nos ícones correspondentes às categorias "Roupas", "Calçados" e "Acessórios".
3. Então o sistema deve exibir os produtos de acordo com a categoria solicitada.

Resultado: A parte correspondente à categoria "Roupas" está correta. No entanto, nas categorias "Calçados" e "Acessórios", os produtos cadastrados correspondentes não são exibidos.

# ID: ZBH-0013 - Verificação de informação

Funcionalidade: Mostrar as informações do produto cadastrado 
Cenário: Na intenção de saber todas as informações fornecidas do produto

Objetivo: Mostrar todas as informações do produto que forem postas na hora do cadastro do produto 

1. Dado que o usuário está logado na plataforma.
2. Quando o usuário busca pela informação fornecidas.
3. Então o sistema deve exibir as informações correspondentes ao produto.
   
Resultado: A informação de frete não aparece na apresentação do produto.
