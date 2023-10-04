#behave --tags=@testeLogin

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
