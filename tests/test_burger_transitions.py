from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver, login_correct

#OK
class TestTransitions:
    def test_transition_designer(self, driver, login_correct):
        driver.find_element(*TestLocators.BUTTON_LK).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            (TestLocators.TEXT_TO_ASSERT_LK)))
        driver.find_element(*TestLocators.BUTTON_DESIGNER).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.ELEMENENT_LOGIN_CHECK))
        current_url = driver.current_url
        expected_url = 'https://stellarburgers.nomoreparties.site/'
        assert current_url == expected_url
        element_main_page = driver.find_element(*TestLocators.ELEMENENT_LOGIN_CHECK).text
        expexted_element = "Соберите бургер"
        assert  expexted_element == element_main_page

    def test_transition_logo(self, driver, login_correct):

        driver.find_element(*TestLocators.BUTTON_LK).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            (TestLocators.TEXT_TO_ASSERT_LK)))
        driver.find_element(*TestLocators.BUTTON_LOGO).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.ELEMENENT_LOGIN_CHECK))
        current_url = driver.current_url
        expected_url = 'https://stellarburgers.nomoreparties.site/'
        assert current_url == expected_url
        element_main_page = driver.find_element(*TestLocators.ELEMENENT_LOGIN_CHECK).text
        expexted_element = "Соберите бургер"
        assert expexted_element == element_main_page
