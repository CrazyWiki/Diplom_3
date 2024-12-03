from pages.main_page import MainPage
from data.urls import Urls

from conftest import driver
from locators.main_page_locators import as MP_locators

class TestMainPage:
    def test_ingredient_popup_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_web_page(Urls.BASE_PAGE_URL)
        main_page.click_any_ingridient()
        text=main_page.check_description_appearence()
        assert text == "Детали ингридиента"

    def test_close_popup_with_cross(self, driver):
        main_page = MainPage(driver)
        main_page.open_web_page(Urls.BASE_PAGE_URL)
        main_page.click_any_ingridient()
        main_page.close_popup_window()

    def test_counter_increment_on_addition(self, driver):
    def test_authenticated_user_can_place_order(self, driver):