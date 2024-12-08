import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators as LP_locators

class LoginPage(BasePage):
    @allure.step("Ввод адреса электронной почты: {email}")
    def enter_email(self, email):
        self.find_element(LP_locators.EMAIL_FIELD).send_keys(email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.find_element(LP_locators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажатие кнопки входа")
    def click_login_button(self):
        self.wait_until_element_is_clickable(LP_locators.LOGIN_BUTTON)
        self.click_element(LP_locators.LOGIN_BUTTON)
