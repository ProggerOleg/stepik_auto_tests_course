import time, math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
button.click()
browser.switch_to.window(browser.window_handles[1])
x = browser.find_element_by_id('input_value').text
x_element = browser.find_element_by_id('answer')
x_element.send_keys(calc(x))
time.sleep(3)