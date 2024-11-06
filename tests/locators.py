from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLocators:
    #Регистрация
    URL_REGISTRATION = "https://stellarburgers.nomoreparties.site/register"
    BUTTON_REGISTRATION = (By.XPATH, './/button[text()="Зарегистрироваться"]')
    INPUT_EMAIL_NAME_PASS = (By.NAME, "name")
    INPUT_PASS = (By.NAME, "Пароль")
    BUTTON_ENTER_LOGIN = (By.XPATH, './/button[text()="Войти"]')
    ALERT_OF_UNCORRECTED_PASS = (By.XPATH, "//*[contains(text(), 'Некорректный пароль')]")

    #Вход
    URL_ENTER_LOGIN = "https://stellarburgers.nomoreparties.site/login"
    BUTTON_ENTER_LOGIN = (By.XPATH, './/button[text()="Войти"]')
    ELEMENENT_LOGIN_CHECK = (By.XPATH, './/h1[text()="Соберите бургер"]')
    BUTTON_LK = (By.XPATH, './/p[text()="Личный Кабинет"]')
    BUTTON_LOGIN_FROM_REGISTRATION = (By.XPATH, './/a[text()="Войти"]')
    URL_RECOVER_PASS = "https://stellarburgers.nomoreparties.site/forgot-password"
    BUTTON_RECOVER_PASS = (By.XPATH, './/button[text()="Восстановить"]')
    #Личный кабинет
    TEXT_TO_ASSERT_LK =(By.XPATH, './/p[text()="В этом разделе вы можете изменить свои персональные данные"]')
    BUTTON_PROFILE = (By.XPATH, './/a[text()="Профиль"]')
    BUTTON_HISTORY_OF_ORDERS = (By.XPATH, './/a[text()="История заказов"]')
    BUTTON_EXIT_FROM_LK = (By.XPATH, './/button[text()="Выход"]')
    #Конструктор и лого бургера
    BUTTON_DESIGNER = (By.XPATH, './/p[text()="Конструктор"]')
    BUTTON_LOGO = (By.XPATH, '//a[@href="/"]')
    # Переходы кнопок булка, начинки и соусы
    BUTTON_ROLLS = (By.XPATH, './/span[text()="Булки"]')
    BUTTON_SAUCE = (By.XPATH, './/span[text()="Соусы"]')
    BUTTON_FILLING = (By.XPATH, './/span[text()="Начинки"]')
    SAUCE_NAME_1 = (By.XPATH, './/p[text()="Соус фирменный Space Sauce"]')
    SAUCE_NAME_2 = (By.XPATH, './/p[text()="Соус традиционный галактический"]')
    ROLLS_NAME_1 = (By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]')
    ROLLS_NAME_2 = (By.XPATH, './/p[text()="Краторная булка N-200i"]')
    FILLING_NAME_1 = (By.XPATH, './/p[text()="Мясо бессмертных моллюсков Protostomia"]')
    FILLING_NAME_2 = (By.XPATH, './/p[text()="Говяжий метеорит (отбивная)"]')


