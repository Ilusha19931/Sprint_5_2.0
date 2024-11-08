from pickle import TUPLE

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver, login_correct
from function_and_variables import email_login, pass_login
from urls import Urls
#okay
class TestLogin:

    def test_login_correct_from_login(self, driver, login_correct):

        element = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ELEMENENT_LOGIN_CHECK))
        assert element.text == "Соберите бургер"
        current_url = driver.current_url
        expected_url = Urls.URL_MAIN_PAGE
        assert current_url == expected_url

    def test_login_correct_from_lk(self, driver):

        driver.get(Urls.URL_ENTER_LOGIN)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER_LOGIN))
        driver.find_element(*TestLocators.BUTTON_LK).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_NAME_PASS).send_keys(email_login)
        driver.find_element(*TestLocators.INPUT_PASS).send_keys(pass_login)
        driver.find_element(*TestLocators.BUTTON_ENTER_LOGIN).click()
        WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located(TestLocators.ELEMENENT_LOGIN_CHECK))

        element = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ELEMENENT_LOGIN_CHECK))
        assert element.text == "Соберите бургер"
        current_url = driver.current_url
        expected_url = Urls.URL_MAIN_PAGE
        assert current_url == expected_url

    def test_login_correct_from_registration(self, driver):

        driver.get(Urls.URL_REGISTRATION)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_REGISTRATION))
        driver.find_element(*TestLocators.BUTTON_LOGIN_FROM_REGISTRATION).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER_LOGIN))
        driver.find_element(*TestLocators.INPUT_EMAIL_NAME_PASS).send_keys(email_login)
        driver.find_element(*TestLocators.INPUT_PASS).send_keys(pass_login)
        driver.find_element(*TestLocators.BUTTON_ENTER_LOGIN).click()
        WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located(TestLocators.ELEMENENT_LOGIN_CHECK))

        element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.ELEMENENT_LOGIN_CHECK))
        assert element.text == "Соберите бургер"
        current_url = driver.current_url
        expected_url = Urls.URL_MAIN_PAGE
        assert current_url == expected_url

    def test_login_correct_from_recover_pass(self, driver):

        driver.get(Urls.URL_RECOVER_PASS)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_RECOVER_PASS))
        driver.find_element(*TestLocators.BUTTON_LOGIN_FROM_REGISTRATION).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER_LOGIN))
        driver.find_element(*TestLocators.INPUT_EMAIL_NAME_PASS).send_keys(email_login)
        driver.find_element(*TestLocators.INPUT_PASS).send_keys(pass_login)
        driver.find_element(*TestLocators.BUTTON_ENTER_LOGIN).click()
        WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located(TestLocators.ELEMENENT_LOGIN_CHECK))

        element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.ELEMENENT_LOGIN_CHECK))
        assert element.text == "Соберите бургер"
        current_url = driver.current_url
        expected_url = Urls.URL_MAIN_PAGE
        assert current_url == expected_url