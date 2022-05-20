from selenium import webdriver
import os, time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    fst_name = browser.find_element_by_css_selector("[name='firstname']")
    fst_name.send_keys('Oleh')

    lst_name = browser.find_element_by_css_selector("[name='lastname']")
    lst_name.send_keys('Tar')

    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys('oleg@bitch.gmail.com')

    button = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")
    button.send_keys(os.path.join(current_dir, 'test.txt'))

    button = browser.find_element_by_tag_name("button")
    button.click()
    text = browser.switch_to.alert.text
    print(text)
    time.sleep(5)

finally:
    browser.close()



