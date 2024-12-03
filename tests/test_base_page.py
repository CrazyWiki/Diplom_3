import allure

from pages.base_page import BasePage
from data.urls import Urls
from locators.base_page_locators import BasePageLocators as BP_locators


class TestBasePage:
    @allure.title("Проверка клика на кнопку 'Конструктор'")
    @allure.description("Кликнуть на кнопку 'Конструктор' и проверить переход на страницу конструктора")
    def test_click_constructor_button(self, driver):
        base_page = BasePage(driver)
        base_page.open_web_page(Urls.LOGIN_PAGE_URL)
        base_page.click_element(BP_locators.CONSTRUCTOR_LINK)
        base_page.wait_until_element_is_clickable(BP_locators.CONSTRUCTOR_LINK)
        assert base_page.get_curent_url() == Urls.BASE_PAGE_URL

    @allure.title("Проверка клика на кнопку 'Лента заказов'")
    @allure.description("Кликнуть на кнопку 'Лента заказов' и проверить переход на страницу ленты заказов")
    def test_click_order_feed_button(self, driver):
        base_page = BasePage(driver)
        base_page.open_web_page(Urls.BASE_PAGE_URL)
        base_page.click_element(BP_locators.ORDER_FEED_LINK)
        base_page.wait_until_element_is_clickable(BP_locators.ORDER_FEED_LINK)
        assert base_page.get_curent_url() == Urls.FEED_PAGE_URL

