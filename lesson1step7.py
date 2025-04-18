from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)         
    
    sunduk = browser.find_element(By.ID, 'treasure')
    x = sunduk.get_attribute("valuex")
    y = calc(x)
   
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y) 
    
    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()
    
    option2 = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    option2.click()    
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)

    # закрываем браузер после всех манипуляций
    browser.quit()