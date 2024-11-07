from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver
from function_and_variables import random_pass_correct, random_email, random_string, random_pass_uncorrect
from urls import Urls
#OK
class TestRegistration:

    def test_register_new_correct(self, driver):

        driver.get(Urls.URL_REGISTRATION)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_REGISTRATION))
        driver.find_elements(*TestLocators.INPUT_EMAIL_NAME_PASS)[0].send_keys(random_string)
        driver.find_elements(*TestLocators.INPUT_EMAIL_NAME_PASS)[1].send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASS).send_keys(random_pass_correct)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_REGISTRATION))
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER_LOGIN))
        current_url = driver.current_url
        expected_url = 'https://stellarburgers.nomoreparties.site/login'
        assert current_url == expected_url

    def test_register_new_uncorrect(self, driver):

        driver.get(Urls.URL_REGISTRATION)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_REGISTRATION))
        driver.find_elements(*TestLocators.INPUT_EMAIL_NAME_PASS)[0].send_keys(random_string)
        driver.find_elements(*TestLocators.INPUT_EMAIL_NAME_PASS)[1].send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASS).send_keys(random_pass_uncorrect)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_REGISTRATION))
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_REGISTRATION))
        current_url = driver.current_url
        expected_url = 'https://stellarburgers.nomoreparties.site/register'
        assert current_url == expected_url
        error_pass = driver.find_element(*TestLocators.ALERT_OF_UNCORRECTED_PASS).text
        assert  error_pass == 'Некорректный пароль'






