from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pytest


class TestMainPage1(object):
    def setup_method(self):
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        self.browser.quit()

    @pytest.mark.parametrize('lincs', ["linc1", "linc2"])
    def test_suite1(self, lincs):

        lincs = ["https://stepik.org/lesson/236895/step/1",
                 "https://stepik.org/lesson/236896/step/1"]
        self.browser.get(lincs)
        self.browser.implicitly_wait(15)
        input1 = self.browser.find_element_by_css_selector('.textarea')

        input1.send_keys(str(math.log(int(time.time()+0.5))))
        #time.sleep(5)

        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
        button.click()
        self.browser.implicitly_wait(5)
        message = self.browser.find_element_by_css_selector(".smart-hints__hint")

        assert "Correct!" in message.text