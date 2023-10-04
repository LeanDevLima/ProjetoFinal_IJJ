#source projetols/Scripts/activate
# ID: ZBH-0012 - Filtrar por produto

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
