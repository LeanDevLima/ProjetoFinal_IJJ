Feature: Acessar categorias de produtos

  @testeLogin
  Scenario: Fazer login
    Given o usuário está na página inicial
    When o usuário insere os dados para login, email e senha
    And o usuário clica no botão Iniciar sessão
    Then o sistema permite o login e fecha o navegador
