import allure
import data.data as Data
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators as PRP_locators


class PasswordRecoveryPage(BasePage):
    @allure.step("Навигация на страницу восстановления пароля")
    def password_recovery_page_navigation(self):
        self.wait_until_element_is_clickable(PRP_locators.LINK_RECOVERY_PASSWORD)
        self.click_element(PRP_locators.LINK_RECOVERY_PASSWORD)
        current_url = self.get_curent_url()
        return current_url

    @allure.step("Ввод электронной почты и подтверждение восстановления пароля")
    def password_recovery_email_input_and_submit(self):
        self.input_data_to_field(PRP_locators.INPUT_EMAIL_FIELD, Data.TEST_EMAIL)
        self.click_element(PRP_locators.BUTTON_RECOVERY_PASSWORD)
        self.wait_until_element_is_visible(PRP_locators.BUTTON_SAVE_NEW_PASSWORD)
        current_url = self.get_curent_url()
        return current_url

    @allure.step("Проверка отображения/скрытия поля пароля")
    def show_hide_password_field(self):
        self.input_data_to_field(PRP_locators.INPUT_EMAIL_FIELD, Data.TEST_EMAIL)
        self.click_element(PRP_locators.BUTTON_RECOVERY_PASSWORD)
        self.click_element(PRP_locators.INPUT_ICON)
        if self.wait_until_element_is_visible_return(PRP_locators.INPUT_PASSWORD_STATUS):
            return True
        else:
            return False
