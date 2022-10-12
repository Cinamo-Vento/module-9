import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text

    # Считать математическую функцию def(x)
    y = calc(x)

    # Ввести ответ в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    #Отметить чекбокс #robotCheckbox
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    #Выбрать radiobutton "Robots rule!"
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    #Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()