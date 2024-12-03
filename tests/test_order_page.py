import time
import allure
import pytest

from pages.order_page import OrderPage
from data.urls import Urls
from locators.order_page_locators import OrderPageLocators as OP_locators
from locators.base_page_locators import BasePageLocators as BP_locators


class TestOrderPage:
    @allure.title("Клик по заказу открывает всплывающее окно с деталями")
    @allure.description(
        "Открывает страницу ленты заказов, кликает по заказу и проверяет наличие деталей заказа в всплывающем окне.")
    def test_click_order_opens_details_popup(self, driver):
        order_page = OrderPage(driver)
        order_page.open_web_page(Urls.FEED_PAGE_URL)
        order_page.click_order_button()
        details_page = order_page.check_order_details()
        assert details_page == True

    @allure.title("Заказы пользователя появляются в ленте заказов")
    @allure.description("Создает новый заказ и проверяет, что он отображается в ленте заказов.")
    def test_user_orders_appear_in_order_feed(self, driver, create_user, delete_user, login_user):
        order_page = OrderPage(driver)
        time.sleep(2)
        order_page.open_web_page(Urls.BASE_PAGE_URL)
        order_id = order_page.make_order()
        order_page.open_web_page(Urls.BASE_PAGE_URL)
        result = order_page.get_order_id_in_feed(order_id)
        assert result == True

    @pytest.mark.parametrize("counter",[OP_locators.TOTAL_ORDERS_ALL_TIME,OP_locators.DAILY_ORDERS_SUMMARY])
    @allure.title("Создание заказа увеличивает счетчик завершенных заказов")
    @allure.description("Проверяет, что при создании нового заказа счетчик успешно увеличивается.")
    def test_create_order_increments_total_completed_counter(self, driver, create_user, delete_user, login_user,counter):
        order_page = OrderPage(driver)
        time.sleep(2)
        order_page.open_web_page(Urls.FEED_PAGE_URL)
        counter1 = order_page.check_counter_feed_order(counter)
        order_page.open_web_page(Urls.BASE_PAGE_URL)
        order_id = order_page.make_order()
        order_page.open_web_page(Urls.FEED_PAGE_URL)
        counter2 = order_page.check_counter_feed_order(counter)
        assert counter1 < counter2

    @allure.title("Номер заказа появляется в процессе после размещения")
    @allure.description(
        "Создает новый заказ и проверяет, что его номер появился в активных заказах, но не в завершенных.")
    def test_order_number_appears_in_progress_after_placement(self, driver, create_user, delete_user, login_user):
        order_page = OrderPage(driver)
        time.sleep(2)
        order_page.open_web_page(Urls.BASE_PAGE_URL)
        order_id = order_page.make_order()
        order_page.click_element(BP_locators.ORDER_FEED_LINK)
        order_page.wait_until_element_is_visible(OP_locators.ACTIVE_ORDERS_COUNT)
        orders_in_process = f"#{order_page.get_text_of_element(OP_locators.ACTIVE_ORDERS_COUNT)}"
        orders_complete = f"#{order_page.get_text_of_element(OP_locators.ACTIVE_ORDERS_COUNT_2)}"
        assert f"{order_id}" in orders_in_process and f"{order_id}" not in orders_complete



