from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver, login_correct
from urls import Urls
#okay
class TestLK:
    def test_exit_from_lk(self, driver, login_correct):
        driver.find_element(*TestLocators.BUTTON_LK).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            (TestLocators.TEXT_TO_ASSERT_LK)))
        driver.find_element(*TestLocators.BUTTON_EXIT_FROM_LK).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER_LOGIN))
        current_url = driver.current_url
        excepted_url = Urls.URL_ENTER_LOGIN
        assert current_url == excepted_url