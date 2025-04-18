from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button_book = browser.find_element(By.ID, "book")
    element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )    
    button_book.click()

    browser.execute_script("window.scrollBy(0, 200);")
    num = browser.find_element(By.ID, 'input_value')
    x = num.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(f'{y}')

    button_submit = browser.find_element(By.ID, "solve")
    button_submit.click()

finally:
    time.sleep(15)
    browser.quit()