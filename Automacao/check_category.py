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