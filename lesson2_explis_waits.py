from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(" http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
wait = WebDriverWait(browser, 5).until(
        EC.((By.ID, "price"), '100'))
button = browser.find_element_by_tag_name("button")
button.click()
x = browser.find_element_by_id('input_value').text
x_element = browser.find_element_by_id('answer')
x_element.send_keys(calc(x))
