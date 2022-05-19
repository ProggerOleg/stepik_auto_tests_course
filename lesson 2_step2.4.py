from selenium import webdriver
import math, time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element_by_id('input_value').text
x_element = browser.find_element_by_id('answer')
x_element.send_keys(calc(x))
browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)

chbox = browser.find_element_by_id('robotCheckbox')
chbox.click()

rdbox = browser.find_element_by_id('robotsRule')
rdbox.click()

button = browser.find_element_by_tag_name("button")
button.click()
time.sleep(5)