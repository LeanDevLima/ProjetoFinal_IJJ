# ID: ZBH-0012 - Filtrar por produto

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