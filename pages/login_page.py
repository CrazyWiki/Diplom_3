import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

import data.data
from locators.login_page_locators import LoginPageLocators as LP_locators
from locators.base_page_locators import BasePageLocators as BP_locators
class LoginPage(BasePage):
    @allure.step("Ввод адреса электронной почты: {email}")
    def enter_email(self, email):
        self.driver.find_element(*LP_locators.EMAIL_FIELD).send_keys(email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.driver.find_element(*LP_locators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажатие кнопки входа")
    def click_login_button(self):
        if data.data.DRIVER_TYPE == "chrome":
            self.driver.find_element(*LP_locators.LOGIN_BUTTON).click()
        elif data.data.DRIVER_TYPE == "firefox":
            WebDriverWait(self.driver, 10).until_not(
                expected_conditions.visibility_of_any_elements_located(BP_locators.MODAL_WINDOW))
            self.driver.find_element(*LP_locators.LOGIN_BUTTON).click()
