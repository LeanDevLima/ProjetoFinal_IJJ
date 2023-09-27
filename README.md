## Plano de Teste - Projeto Final - Bugou? QA tá ON! 📅 📦

Este plano de teste descreve os testes a serem executados no Sistema de Vendas do Instituto Joga Junto, com foco na perspectiva do vendedor. O sistema é composto por uma aplicação frontend construída com React JS, hospedada na AWS Amplify, e utiliza uma estrutura de backend em NodeJS com um banco de dados MySQL versão 8.

**Equipe de QA:** [Inserir nomes da equipe aqui] 👥

**Data de Execução:** [Inserir data de execução aqui] 📅

### Testes de API 🚀

#### 1. Verificação da Disponibilidade da API ✅

**Método:** GET

**Endpoint:** /hearts

**Caso de Teste 1:** Verificar se a API está online 🌎

**Passos:**

1. Realizar uma solicitação GET para /hearts.
2. Verificar se a resposta retorna um código 200 (A API está funcionando corretamente).

**Resultado Esperado:** A API está online. ✅

#### 2. Listagem de Produtos 🛒

**Método:** GET

**Endpoint:** /

**Caso de Teste 2:** Verificar a listagem de produtos 📃

**Passos:**

1. Realizar uma solicitação GET para /.
2. Verificar se a resposta retorna um código 200 (Lista de produtos retornada com sucesso).
3. Verificar se a resposta contém uma lista de produtos válida.

**Resultado Esperado:** Lista de produtos é retornada com sucesso. ✅

#### 3. Cadastro de Produto ➕

**Método:** POST

**Endpoint:** /

**Caso de Teste 3:** Cadastrar um novo produto com sucesso 📦

**Passos:**

1. Autenticar-se como vendedor (usar o caso de teste de login ou registro).
2. Realizar uma solicitação POST para / com os dados do novo produto.
3. Verificar se a resposta retorna um código 200 (Produto cadastrado com sucesso).

**Resultado Esperado:** Produto é cadastrado com sucesso. ✅

**Método:** POST

**Endpoint:** /register

**Caso de Teste 4:** Tentativa de cadastro de produto sem autenticação 🚫

**Passos:**

1. Realizar uma solicitação POST para / sem autenticação.
2. Verificar se a resposta retorna um código 400 (Usuário não encontrado).

**Resultado Esperado:** Erro indicando que o usuário não está autenticado. 🚫

#### 4. Autenticação e Registro de Usuário 👤

**Método:** POST

**Endpoint:** /login

**Caso de Teste 5:** Login bem-sucedido 🔑

**Passos:**

1. Realizar uma solicitação POST para /login com credenciais válidas.
2. Verificar se a resposta retorna um código 200 (Login bem-sucedido).

**Resultado Esperado:** Login é bem-sucedido. ✅

**Método:** POST

**Endpoint:** /login

**Caso de Teste 6: **Tentativa de login com credenciais inválidas ❌

**Passos:**

1. Realizar uma solicitação POST para /login com credenciais inválidas.
2. Verificar se a resposta retorna um código 401 (Credenciais inválidas).

**Resultado Esperado:** Erro indicando que as credenciais são inválidas. ❌

**Método:** POST

**Endpoint:** /register

**Caso de Teste 7:** Registro de novo usuário com sucesso 👤

**Passos:**

1. Realizar uma solicitação POST para /register com dados de novo usuário.
2. Verificar se a resposta retorna um código 200 (Usuário cadastrado com sucesso).

**Resultado Esperado:** Novo usuário é registrado com sucesso. ✅

**Método:** POST

**Endpoint:** /register

**Caso de Teste 8:** Tentativa de registro com um email já cadastrado ⚠️

**Passos:**

1. Realizar uma solicitação POST para /register com um email que já está cadastrado.
2. Verificar se a resposta retorna um código 409 (Email já cadastrado).

**Resultado Esperado:** Erro indicando que o email já está cadastrado. ⚠️

### Testes da Aplicação Principal 💻

#### 1. Fluxo de Login/Logout 🔑

**Caso de Teste 9:** Realizar login e logout com sucesso na aplicação. 🔓

**Passos:**

1. Abrir a aplicação. 💻
2. Realizar o login com credenciais válidas. 🔑
3. Verificar se o login foi bem-sucedido. ✅
4. Realizar o logout. 🚪
5. Verificar se o logout foi bem-sucedido. ✅

**Resultado Esperado:** Login e logout são realizados com sucesso. ✅

#### 2. Cadastro de Produto na Aplicação 📦

**Caso de Teste 10:** Cadastrar um novo produto na aplicação. 📦

**Passos:**

1. Realizar o login como vendedor. 👤
2. Acessar a função de cadastro de produto. 📦
3. Preencher os detalhes do novo produto. ✍️
4. Submeter o formulário de cadastro. 📤
5. Verificar se o produto é cadastrado com sucesso. ✅

**Resultado Esperado:** Novo produto é cadastrado com sucesso. ✅

#### 3. Pesquisa de Produto 🔍

**Caso de Teste 11:** Pesquisar por um produto na aplicação. 🔍

**Passos:**

1. Realizar o login como vendedor. 👤
2. Acessar a função de pesquisa de produto. 🔍
3. Inserir um termo de pesquisa válido. ✏️
4. Verificar se os resultados da pesquisa correspondem ao termo inserido. ✅

**Resultado Esperado:** A pesquisa retorna resultados válidos. ✅

#### 4. Filtragem de Produtos 📅

**Caso de Teste 12:** Aplicar filtros para refinar a lista de produtos. 📦

**Passos:**

1. Realizar o login como vendedor. 👤
2. Acessar a função de filtragem de produtos. 📅
3. Aplicar filtros (por categoria, preço, etc.). 📦
4. Verificar se os produtos exibidos correspondem aos filtros aplicados. ✅

**Resultado Esperado:** Os produtos exibidos são filtrados de acordo com os critérios selecionados. ✅

### Entregas Obrigatórias 📦

- Plano de teste com cenários em Gherkin/BDD
- Bug report com evidência de testes no Bitrix
- Testes das funcionalidades: Fluxo de Login/Logout, Cadastro de Produto, Pesquisa de Produto, Filtragem de Produtos
- Fluxo de navegação na loja
- Testes automatizados (pelo menos um cenário testado de modo automatizado)
- Testes de API (Criar conta e cadastrar um produto através da API via Postman, além de realizar testes básicos, como checar status e verificar elementos)
- Bug report: Reportar individualmente cada bug e criar um relatório contendo a quantidade de bugs classificados por criticidade

### Observações 📅

- Testes de performance, como carga e estresse, não devem ser realizados.
- O sistema pode ficar lento conforme uploads forem feitos, isso não deve ser catalogado como um bug.

### Apresentação 📦

- Cada Squad terá entre 15 e 20 minutos de apresentação.
- Um teste de API e um teste automatizado deverão ser realizados ao vivo, com a opção de gravar um vídeo dos testes funcionando em caso de falha.
- Todos os membros do squad devem participar ativamente da apresentação com a câmera ligada.
- O plano de teste, bug report, repositório e Collection do Postman em JSON devem ser submetidos até 1 hora antes da apresentação.
- Selecionar os bugs mais importantes de cada categoria para apresentação, com no mínimo 1 bug por criticidade.

### Critérios de Avaliação 📅

- Conformidade com o que foi demandado (testes obrigatórios e entregas dentro do prazo)
- Aplicação do conhecimento adquirido no curso
- Participação de todo o squad na apresentação final
- Bom comportamento, dicção e clareza das ideias.
