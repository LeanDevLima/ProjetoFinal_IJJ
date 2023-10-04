from selenium.webdriver.common.by import By

def login(navegador, email, senha):
    campo_email = navegador.find_element(By.NAME, "email")
    campo_email.send_keys(email)

    campo_senha = navegador.find_element(By.NAME, "password")
    campo_senha.send_keys(senha)

