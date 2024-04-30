import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class TestFormyForm(unittest.TestCase):
    SUBMIT_BTN = (By.CSS_SELECTOR, "[role='button']")

    # se ruleaza inainte de fiecare test si are rolul de a face setupul de chrome si eventuale preconditii
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://formy-project.herokuapp.com/form")

    # se ruleaza dupa fiecare test si are rolul de a inchide driverul de chrome
    def tearDown(self):
        self.driver.quit()

    # verificam URL
    @unittest.skip
    def test_url(self):
        actual_url = self.driver.current_url
        expected_url = "https://formy-project.herokuapp.com/form"
        self.assertEqual(expected_url, actual_url, "URL is incorrect")

    def test_page_title(self):
        self.driver.implicitly_wait(10)
        actual_title = self.driver.title
        expected_title = "Formy"
        print(f"Extracted page title is: {actual_title}")
        self.assertEqual(expected_title, actual_title, "Page title is incorrect")

    def test_submit_button_text(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[role='button']")))
        actual_button_text = self.driver.find_element(*self.SUBMIT_BTN).text
        expected_button_text = "Submit"
        print(f"Submit button text is: {actual_button_text}")

        self.assertEqual(expected_button_text, actual_button_text, "Submit btn text is incorrect")













