# ID: ZBH-0012 - Filtrar por produto

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

navegador = Firefox()
navegador.get("https://projetofinal.jogajuntoinstituto.org/")

sleep(3)

campo_email = navegador.find_element(By.NAME, "email")
campo_email.send_keys("leanderson.devlima@gmail.com")

campo_senha = navegador.find_element(By.NAME, "password")
campo_senha.send_keys("jcjcjc@33")

sleep(3)

botao = navegador.find_element(By.XPATH, '//*[@id="root"]/main/form/button')
botao.click()

sleep(3)

def green(message):
    print("\033[92m" + message + "\033[0m")

def red(message):
    print("\033[91m" + message + "\033[0m")

def click_link_and_check_success(navegador, link_xpath, item_name):
    try:
        link = navegador.find_element(By.XPATH, link_xpath)
        link.click()
        sleep(3)
        if item_name in navegador.page_source:
            green(f"Link '{item_name}' foi bem-sucedido!")
        else:
            raise NoSuchElementException("Elemento não encontrado")
    except NoSuchElementException:
        red(f"Link '{item_name}' não foi bem-sucedido! (Elemento não encontrado)")


click_link_and_check_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[2]/li', "Roupas")
click_link_and_check_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[3]/li', "Calçados")
click_link_and_check_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[4]/li', "Acessórios")

click_link_and_check_success(navegador, '/html/body/div/header/section[2]/nav/ul/div[2]/div[1]/div[5]/li', "Elemento Inexistente")

sleep(3)

navegador.quit()
