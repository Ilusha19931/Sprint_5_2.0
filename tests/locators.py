from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLocators:
    #Регистрация
    URL_REGISTRATION = "https://stellarburgers.nomoreparties.site/register"
    BUTTON_REGISTRATION = (By.XPATH, './/a[text()="Зарегистрироваться"]')
    INPUT_EMAIL_NAME = (By.NAME, "name")
    INPUT_PASSWORD = (By.NAME, "password")
    BUTTON_ENTER_LOGIN = (By.XPATH, './/button[text()="Войти"]')

    #Вход
    URL_ENTER_LOGIN = "https://stellarburgers.nomoreparties.site/login"
    BUTTON_ENTER_LOGIN = (By.XPATH, './/button[text()="Войти"]')

