import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Post(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_post(self):
        user = "nwade"
        pwd = "Neva3490"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/div[1]/a/span").click()
        time.sleep(3)

        title = "Selenium Test"
        post = "This is a selenium test"
        elem = driver.find_element_by_id("id_title")
        elem.send_keys(title)
        time.sleep(3)

        elem = driver.find_element_by_id("id_text")
        elem.send_keys(post)
        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        assert "Posted Blog Entry"
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)
        driver.get("http://127.0.0.1:8000")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
            unittest.main()
