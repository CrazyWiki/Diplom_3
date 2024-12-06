import time
import allure

import data.data
from pages.main_page import MainPage
from data.urls import Urls
from locators.main_page_locators import ManePageLocators as MP_locators
from locators.base_page_locators import BasePageLocators as BP_locators

class TestMainPage:

    @allure.title("Проверка клика на кнопку 'Конструктор'")
    @allure.description("Кликнуть на кнопку 'Конструктор' и проверить переход на страницу конструктора")
    def test_click_constructor_button(self, driver):
        base_page = MainPage(driver)
        base_page.open_web_page(Urls.LOGIN_PAGE_URL)
        base_page.click_element(BP_locators.CONSTRUCTOR_LINK)
        base_page.wait_until_element_is_clickable(BP_locators.CONSTRUCTOR_LINK)
        assert base_page.get_curent_url() == Urls.BASE_PAGE_URL

    @allure.title("Проверка клика на кнопку 'Лента заказов'")
    @allure.description("Кликнуть на кнопку 'Лента заказов' и проверить переход на страницу ленты заказов")
    def test_click_order_feed_button(self, driver):
        base_page = MainPage(driver)
        base_page.open_web_page(Urls.BASE_PAGE_URL)
        base_page.click_element(BP_locators.ORDER_FEED_LINK)
        base_page.wait_until_element_is_clickable(BP_locators.ORDER_FEED_LINK)
        assert base_page.get_curent_url() == Urls.FEED_PAGE_URL


    @allure.title("Проверка попап окна с информацией об ингредиенте")
    def test_ingredient_popup_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_web_page(Urls.BASE_PAGE_URL)
        main_page.click_any_ingridient()
        text=main_page.check_description_appearence()
        assert text == "Детали ингредиента"

    @allure.description("Проверка закрытия попап окна крестиком")
    def test_close_popup_with_cross(self, driver):
        main_page = MainPage(driver)
        main_page.open_web_page(Urls.BASE_PAGE_URL)
        main_page.click_any_ingridient()
        main_page.close_popup_window()
        invisibility= main_page.check_invisibility_of_element(element=MP_locators.INGREDIENT_DETAILS_IN_POPUP)
        assert invisibility == True

    @allure.title("Проверка увеличения счетчика при добавлении ингредиента")  # Title in Russian
    def test_counter_increment_on_addition(self, driver):
        main_page = MainPage(driver)
        main_page.open_web_page(Urls.BASE_PAGE_URL)
        first_value_counter = main_page.get_ingredient_count_value()
        main_page.add_filling_to_order()
        time.sleep(2)
        second_value_counter = main_page.get_ingredient_count_value()
        assert first_value_counter < second_value_counter

    @allure.title("Проверка возможности оформления заказа авторизованным пользователем")  # Title in Russian
    def test_authenticated_user_can_place_order(self, driver,create_user,delete_user,login_user):
        main_page = MainPage(driver)
        #main_page.open_web_page(Urls.LOGIN_PAGE_URL)
        #main_page.login_user(create_user[0],create_user[1])
        time.sleep(2)
        main_page.add_filling_to_order()
        time.sleep(2)
        main_page.click_order_button()
        id = main_page.get_order_id()
        assert id != data.data.ORDER_ID_BY_DEFAULT
