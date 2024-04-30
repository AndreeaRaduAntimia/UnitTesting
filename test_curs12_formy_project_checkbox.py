import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestFormyCheckbox(unittest.TestCase):
    CHECKBOX1 = (By.ID, "checkbox-1")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://formy-project.herokuapp.com/checkbox")

    # se ruleaza dupa fiecare test si are rolul de a inchide driverul de chrome
    def tearDown(self):
        self.driver.quit()

    def test_first_checkbox_is_selected(self):
        checkbox1 = self.driver.find_element(*self.CHECKBOX1)
        checkbox1.click()
        self.assertTrue(checkbox1.is_selected())



