import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from random_function import random_pass_correct, random_email, random_string
from locators import TestLocators
from tests.conftest import driver, redister_new_correct


class TestRegistration:

    def redister_new_correct_test(self, driver):

        driver.find_elements(TestLocators.INPUT_EMAIL_NAME)[0].send_keys(random_string)
        time.sleep(3)
        driver.find_elements(TestLocators.INPUT_EMAIL_NAME)[1].send_keys(random_email)
        time.sleep(3)
        driver.find_elements(TestLocators.INPUT_PASSWORD).send_keys(random_pass_correct)
        time.sleep(3)
        driver.find_element(TestLocators.BUTTON_REGISTRATION).click()

        current_url = driver.current_url
        expected_url = 'https://stellarburgers.nomoreparties.site/'
        assert current_url == expected_url



test_for_work = TestRegistration()
test_for_work.redister_new_correct_test(driver)


