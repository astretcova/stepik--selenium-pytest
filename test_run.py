from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pytest


class TestMainPage1(object):
    #browser = None
    def setup_method(self):
        print("\nstart browser for test suite1")
        self.browser = webdriver.Chrome()
        self.button = None

    def teardown_method(self):
        print("quit browser for test suite1")
        self.browser.quit()

    def test_suite1(self):
        # link = "https://stepik.org/lesson/236895/step/1"
        self.browser.get("https://stepik.org/lesson/236895/step/1")
        self.browser.implicitly_wait(5)
        input1 = self.browser.find_element_by_css_selector('.textarea')
        # input1 = browser.find_element_by_xpath('//*[@id="answer"]')
        input1.send_keys(str(math.log(int(time.time()+0.5))))
        #time.sleep(5)

        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
        button.click()
        self.browser.implicitly_wait(5)
        message = self.browser.find_element_by_css_selector(".smart-hints__hint")

        assert "Correct!" in message.text

    def test_suite2(self):
        # link = "https://stepik.org/lesson/236895/step/1"
        self.browser.get("https://stepik.org/lesson/236896/step/1")
        self.browser.implicitly_wait(5)
        input1 = self.browser.find_element_by_css_selector('[placeholder]')
        # input1 = browser.find_element_by_xpath('//*[@id="answer"]')
        input1.send_keys(str(math.log(int(time.time() + 0.5))))
        # time.sleep(5)

        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ember56 > div > section > div > div.attempt__inner > div.attempt__actions > button"))
        )
        button.click()
        self.browser.implicitly_wait(5)
        message = self.browser.find_element_by_css_selector("#ember76 > pre")

        assert "Correct!" in message.text

    def test_suite3(self):
        # link = "https://stepik.org/lesson/236895/step/1"
        self.browser.get("https://stepik.org/lesson/236897/step/1")
        self.browser.implicitly_wait(5)
        input1 = self.browser.find_element_by_css_selector('[placeholder]')
        # input1 = browser.find_element_by_xpath('//*[@id="answer"]')
        input1.send_keys(str(math.log(int(time.time() + 0.5))))
        # time.sleep(5)

        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#ember56 > div > section > div > div.attempt__inner > div.attempt__actions > button"))
        )
        button.click()
        self.browser.implicitly_wait(5)
        message = self.browser.find_element_by_css_selector("#ember76 > pre")

        assert "Correct!" in message.text

    def test_suite4(self):
        # link = "https://stepik.org/lesson/236895/step/1"
        self.browser.get("https://stepik.org/lesson/236898/step/1")
        self.browser.implicitly_wait(5)
        input1 = self.browser.find_element_by_css_selector('[placeholder]')
        # input1 = browser.find_element_by_xpath('//*[@id="answer"]')
        input1.send_keys(str(math.log(int(time.time() + 0.5))))
        # time.sleep(5)

        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#ember56 > div > section > div > div.attempt__inner > div.attempt__actions > button"))
        )
        button.click()
        self.browser.implicitly_wait(5)
        message = self.browser.find_element_by_css_selector("#ember76 > pre")
        time.sleep(5)

        assert "Correct!" in message.text
    def test_suite5(self):
        # link = "https://stepik.org/lesson/236895/step/1"
        self.browser.get("https://stepik.org/lesson/236899/step/1")
        self.browser.implicitly_wait(5)
        input1 = self.browser.find_element_by_css_selector('[placeholder]')
        # input1 = browser.find_element_by_xpath('//*[@id="answer"]')
        input1.send_keys(str(math.log(int(time.time() + 0.5))))
        # time.sleep(5)

        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#ember56 > div > section > div > div.attempt__inner > div.attempt__actions > button"))
        )
        button.click()
        self.browser.implicitly_wait(5)
        message = self.browser.find_element_by_css_selector("#ember76 > pre")
        time.sleep(5)

        assert "Correct!" in message.text
    def test_suite6(self):
        # link = "https://stepik.org/lesson/236895/step/1"
        self.browser.get("https://stepik.org/lesson/236903/step/1")
        self.browser.implicitly_wait(5)
        input1 = self.browser.find_element_by_css_selector('[placeholder]')
        # input1 = browser.find_element_by_xpath('//*[@id="answer"]')
        input1.send_keys(str(math.log(int(time.time() + 0.5))))
        # time.sleep(5)

        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#ember56 > div > section > div > div.attempt__inner > div.attempt__actions > button"))
        )
        button.click()
        self.browser.implicitly_wait(5)
        message = self.browser.find_element_by_css_selector("#ember76 > pre")
        time.sleep(5)

        assert "Correct!" in message.text
    def test_suite7(self):
        # link = "https://stepik.org/lesson/236895/step/1"
        self.browser.get("https://stepik.org/lesson/236904/step/1")
        self.browser.implicitly_wait(5)
        input1 = self.browser.find_element_by_css_selector('[placeholder]')
        # input1 = browser.find_element_by_xpath('//*[@id="answer"]')
        input1.send_keys(str(math.log(int(time.time() + 0.5))))
        # time.sleep(5)

        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#ember56 > div > section > div > div.attempt__inner > div.attempt__actions > button"))
        )
        button.click()
        self.browser.implicitly_wait(5)
        message = self.browser.find_element_by_css_selector("#ember76 > pre")
        time.sleep(5)

        assert "Correct!" in message.text
    def test_suite8(self):
        # link = "https://stepik.org/lesson/236895/step/1"
        self.browser.get("https://stepik.org/lesson/236905/step/1")
        self.browser.implicitly_wait(5)
        input1 = self.browser.find_element_by_css_selector('[placeholder]')
        # input1 = browser.find_element_by_xpath('//*[@id="answer"]')
        input1.send_keys(str(math.log(int(time.time() + 0.5))))
        # time.sleep(5)

        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#ember56 > div > section > div > div.attempt__inner > div.attempt__actions > button"))
        )
        button.click()
        self.browser.implicitly_wait(5)
        message = self.browser.find_element_by_css_selector("#ember76 > pre")
        time.sleep(5)

        assert "Correct!" in message.text