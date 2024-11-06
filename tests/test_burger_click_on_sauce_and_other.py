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
    def test_tap_on_sauce(self, driver, login_correct):
        driver.find_element(*TestLocators.BUTTON_SAUCE).click()
        sauce_name_1 = driver.find_element(*TestLocators.SAUCE_NAME_1)
        sauce_name_2 = driver.find_element(*TestLocators.SAUCE_NAME_2)
        assert sauce_name_1.text == "Соус фирменный Space Sauce"
        assert sauce_name_2.text == "Соус традиционный галактический"

    def test_tap_on_rolls(self, driver, login_correct):
        driver.find_element(*TestLocators.BUTTON_SAUCE).click()
        driver.find_element(*TestLocators.BUTTON_ROLLS).click()
        rolls_name_1 = driver.find_element(*TestLocators.ROLLS_NAME_1)
        rolls_name_2 = driver.find_element(*TestLocators.ROLLS_NAME_2)
        assert rolls_name_1.text == "Флюоресцентная булка R2-D3"
        assert rolls_name_2.text == "Краторная булка N-200i"

    def test_tap_on_filling(self, driver, login_correct):
        driver.find_element(*TestLocators.BUTTON_FILLING).click()
        filling_name_1 = driver.find_element(*TestLocators.FILLING_NAME_1)
        filling_name_2 = driver.find_element(*TestLocators.FILLING_NAME_2)
        assert filling_name_1.text == "Мясо бессмертных моллюсков Protostomia"
        assert filling_name_2.text == "Говяжий метеорит (отбивная)"

