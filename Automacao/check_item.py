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