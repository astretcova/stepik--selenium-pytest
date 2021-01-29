import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains

link = "https://yandex.ru/"


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def check_two_pages(browser):
    return len(browser.window_handles) == 2


def test_one(browser):
    browser.get(link)
    input = browser.find_element_by_css_selector("#text")
    input.send_keys('ViPNet Coordinator HW5000')
    input.send_keys(Keys.ESCAPE)
    button = browser.find_element_by_css_selector("div.search2__button")
    button.click()
    browser.implicitly_wait(5)
    open_pdf = browser.find_element_by_css_selector(
        '[href="https://infotecs.ru/upload/iblock/db0/ViPNet_Coordinator_HW_5000_web_july_2018.pdf"')
    ActionChains(browser).move_to_element(open_pdf) \
        .key_down(Keys.CONTROL).click(open_pdf).key_up(Keys.CONTROL).perform()
    wait(browser, 10).until(check_two_pages)
    browser.switch_to_window(browser.window_handles[1])
