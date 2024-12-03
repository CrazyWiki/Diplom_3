import allure

from pages.password_recovery_page import PasswordRecoveryPage
from data.urls import Urls
from locators.password_recovery_locators import PasswordRecoveryLocators as PRP_locators
class TestPasswordRecovery:
    @allure.title("Навигация на страницу восстановления пароля")
    @allure.description(
        "Открывает страницу входа, затем переходит на страницу восстановления пароля и проверяет текущий URL.")
    def test_password_recovery_page_navigation(self, driver):
        password_recovery_page  = PasswordRecoveryPage(driver)
        password_recovery_page.open_web_page(Urls.LOGIN_PAGE_URL)
        password_recovery_page.wait_until_element_is_clickable(PRP_locators.LINK_RECOVERY_PASSWORD)
        current_url = password_recovery_page.password_recovery_page_navigation()
        assert current_url == (f"{Urls.RESTORE_PASSWORD_PAGE_URL}")

    @allure.title("Ввод email и отправка запроса на восстановление пароля")
    @allure.description(
        "Открывает страницу сброса пароля, вводит email и отправляет запрос, затем проверяет текущий URL.")
    def test_email_input_and_submit(self,driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open_web_page(f"{Urls.RESET_PASSWORD_PAGE_URL}")
        current_url = password_recovery_page.password_recovery_email_input_and_submit()
        assert current_url == (f"{Urls.RESET_PASSWORD_PAGE_URL}")

    @allure.title("Показать/скрыть поле пароля")
    @allure.description(
        "Открывает страницу сброса пароля и проверяет, меняется ли видимость поля пароля при взаимодействии.")
    def test_show_hide_password_field(self,driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open_web_page(Urls.RESET_PASSWORD_PAGE_URL)
        recovery_bool = password_recovery_page.show_hide_password_field()
        assert recovery_bool is True

