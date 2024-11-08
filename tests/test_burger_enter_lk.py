from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver, login_correct

#okay
class TestLK:
    def test_enter_lk(self, driver, login_correct):
        driver.find_element(*TestLocators.BUTTON_LK).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            (TestLocators.TEXT_TO_ASSERT_LK)))
        profile = driver.find_element(*TestLocators.BUTTON_PROFILE)
        history_deliveri = driver.find_element(*TestLocators.BUTTON_HISTORY_OF_ORDERS)
        info_about_lk = driver.find_element(*TestLocators.TEXT_TO_ASSERT_LK)
        assert profile.text == "Профиль"
        assert history_deliveri.text == "История заказов"
        assert info_about_lk.text == "В этом разделе вы можете изменить свои персональные данные"