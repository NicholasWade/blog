import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AdminPostAndDelete(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_and_delete_all(self):
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
        driver.get("http://127.0.0.1:8000/admin")
        assert "Logged In"
        time.sleep(3)

        driver.get("http://127.0.0.1:8000/admin/blog/post")
        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
        time.sleep(2)

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[1]/div/div/select/option[2]").click()
        time.sleep(2)

        title = "Selenium Test"
        post = "This is a selenium test"
        elem = driver.find_element_by_id("id_title")
        elem.send_keys(title)
        time.sleep(3)

        elem = driver.find_element_by_id("id_text")
        elem.send_keys(post)
        time.sleep(2)

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/admin/blog/post")
        time.sleep(3)

        elem = driver.find_element_by_id("action-toggle").click()
        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/label/select/option[2]").click()
        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/button").click()
        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[4]").click()
        time.sleep(3)

        assert "Deleted All Blog Entries"
        driver.get("http://127.0.0.1:8000/admin/blog/post")
        time.sleep(5)
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
            unittest.main()
