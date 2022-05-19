from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1').text
    y_element = browser.find_element_by_id('num2').text
    y = int(x_element) + int(y_element)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))

    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(5)
finally:
    browser.close()
