import allure
import time
import data.data as Data
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators as PRP_locators


class PasswordRecoveryPage(BasePage):
    @allure.title("Навигация на страницу восстановления пароля")
    @allure.description("Нажимает на ссылку для восстановления пароля и возвращает текущий URL.")
    def password_recovery_page_navigation(self):
        self.click_element(PRP_locators.LINK_RECOVERY_PASSWORD)
        current_url = self.get_curent_url()
        return current_url

    @allure.title("Ввод email для восстановления пароля и отправка")
    @allure.description(
        "Вводит адрес электронной почты в поле и отправляет запрос на восстановление пароля, затем возвращает текущий URL.")
    def password_recovery_email_input_and_submit(self):
        self.input_data_to_field(PRP_locators.INPUT_EMAIL_FIELD, Data.TEST_EMAIL)
        self.click_element(PRP_locators.BUTTON_RECOVERY_PASSWORD)
        self.wait_until_element_is_visible(PRP_locators.RECOVERY_PASSWORD_LABEL)
        time.sleep(2)
        current_url = self.get_curent_url()
        return current_url

    @allure.title("Показать/скрыть поле пароля")
    @allure.description(
        "Вводит email, нажимает на кнопку восстановления пароля, затем переключает отображение поля пароля и проверяет его статус.")
    def show_hide_password_field(self):
        self.input_data_to_field(PRP_locators.INPUT_EMAIL_FIELD, Data.TEST_EMAIL)
        self.click_element(PRP_locators.BUTTON_RECOVERY_PASSWORD)
        self.click_element(PRP_locators.INPUT_ICON)
        time.sleep(2)
        if self.wait_until_element_is_visible_return(PRP_locators.INPUT_PASSWORD_STATUS):
            return True
        else:
            return False
