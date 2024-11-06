import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from function_and_variables import random_pass_correct, random_email, random_string, email_login, pass_login
from locators import TestLocators
from conftest import driver, login_correct
from tests.function_and_variables import random_pass_uncorrect, email_login, pass_login

class TestLK:
    def test_exit_from_lk(self, driver, login_correct):
        driver.find_element(*TestLocators.BUTTON_LK).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            (TestLocators.TEXT_TO_ASSERT_LK)))
        driver.find_element(*TestLocators.BUTTON_EXIT_FROM_LK).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER_LOGIN))
        current_url = driver.current_url
        excepted_url = 'https://stellarburgers.nomoreparties.site/login'
        assert current_url == excepted_url