import unittest
from selenium import webdriver
import time


class TestForm(unittest.TestCase):
    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys("email")
        input4 = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[1]/input')
        input4.send_keys("email")
        input5 = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[2]/input')
        input5.send_keys("email")

        button = browser.find_element_by_xpath('/html/body/div/form/button')
        button.click()
        time.sleep(1)
        welcom_text_elt = browser.find_element_by_xpath('/html/body/div')
        welcom_text = welcom_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcom_text, 'совпадает')
        time.sleep(1)
        browser.quit()

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.htmlpytest test_abs_project.py"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys("email")
        input4 = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[1]/input')
        input4.send_keys("email")
        input5 = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[2]/input')
        input5.send_keys("email")

        button = browser.find_element_by_xpath('/html/body/div/form/button')
        button.click()
        time.sleep(1)
        welcom_text_elt = browser.find_element_by_xpath('/html/body/div')
        welcom_text = welcom_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcom_text, 'совпадает')
        time.sleep(1)
        browser.quit()


if __name__ == "__main__":
    unittest.main()