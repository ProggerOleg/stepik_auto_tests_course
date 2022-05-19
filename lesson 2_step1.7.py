from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    inp = browser.find_element_by_id('answer')
    inp.send_keys(y)

    chbox = browser.find_element_by_id('robotCheckbox')
    chbox.click()

    rdbox = browser.find_element_by_id('robotsRule')
    rdbox.click()

    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(5)
finally:
    browser.close()
