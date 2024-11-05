import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from random_function import random_pass_correct, random_email, random_string
from locators import TestLocators
@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()

@pytest.fixture
def redister_new_correct(driver):

    driver.get(TestLocators.URL_REGISTRATION)

    driver.find_element(TestLocators.INPUT_EMAIL_NAME_PASS).send_keys(random_string)
    driver.find_element(TestLocators.INPUT_EMAIL_NAME_PASS).send_keys(random_email)
    driver.find_element(TestLocators.INPUT_EMAIL_NAME_PASS).send_keys(random_pass_correct)

    driver.find_element(TestLocators.BUTTON_REGISTRATION).click()