import time
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from function_and_variables import email_login, pass_login
from locators import TestLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver

    driver.quit()

@pytest.fixture
def login_correct(driver):
    driver.get(TestLocators.URL_ENTER_LOGIN)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER_LOGIN))
    driver.find_element(*TestLocators.INPUT_EMAIL_NAME_PASS).send_keys(email_login)
    driver.find_element(*TestLocators.INPUT_PASS).send_keys(pass_login)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER_LOGIN))
    driver.find_element(*TestLocators.BUTTON_ENTER_LOGIN).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.ELEMENENT_LOGIN_CHECK))