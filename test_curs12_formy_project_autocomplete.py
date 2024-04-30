import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFormyAutocomplete(unittest.TestCase):
    CITY_INPUT = (By.ID, "locality")
    NAV_BAR = (By.ID, "navbarDropdownMenuLink")
    MODAL_LINK = (By.CSS_SELECTOR, "[href='/modal']")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://formy-project.herokuapp.com/autocomplete")

    # se ruleaza dupa fiecare test si are rolul de a inchide driverul de chrome
    def tearDown(self):
        self.driver.quit()

    def test_city_input_is_visible(self):
        city_input = self.driver.find_element(*self.CITY_INPUT)
        self.assertTrue(city_input.is_displayed(), "City input is not visible")

    def test_url_waits(self):
        print(self.driver.current_url)
        navbar = self.driver.find_element(*self.NAV_BAR)
        navbar.click()
        modal = self.driver.find_element(*self.MODAL_LINK)
        modal.click()
        print(self.driver.current_url)
        WebDriverWait(self.driver, 5).until((EC.url_contains("/modal")))
        self.assertIn("/modal", self.driver.current_url)







