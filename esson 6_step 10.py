from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_class_name('form-control.first')
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_class_name('form-control.second')
    input2.send_keys("Petrov")

    inpute = browser.find_element_by_class_name('form-control.third')
    inpute.send_keys("oleg0t@gmail.com")

    inputf = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[1]/input")
    inputf.send_keys("380952506701")

    input5 = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[2]/input")
    input5.send_keys("Pushkina 13")

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1").text
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()