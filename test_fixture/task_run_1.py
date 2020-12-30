import pytest
from selenium import webdriver
import time
import math

#answer = math.log(int(time.time()))

try:
    link = "https://time.is/ru/Moscow"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    time = browser.find_element_by_xpath('//*[@id="time_section"]/div[2]')
    time = time.text
    time = str(time)
    answer = math.log(int(time.time()+0.6))
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
print(answer)