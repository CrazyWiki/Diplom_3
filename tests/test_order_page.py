import allure
import pytest

from pages.order_page import OrderPage
from data.urls import Urls
from locators.order_page_locators import OrderPageLocators as OP_locators
from conftest import driver, create_user, delete_user, login_user


#from conftest import driver, create_user, delete_user, login_user

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
        order_page.open_web_page(Urls.BASE_PAGE_URL)
        order_id = order_page.make_order()
        order_page.open_web_page(Urls.BASE_PAGE_URL)
        result = order_page.get_order_id_in_feed(order_id)
        assert result == True

    @pytest.mark.parametrize("counter", [OP_locators.TOTAL_ORDERS_ALL_TIME, OP_locators.DAILY_ORDERS_SUMMARY])
    @allure.title("Создание заказа увеличивает счетчик завершенных заказов")
    @allure.description("Проверяет, что при создании нового заказа счетчик успешно увеличивается.")
    def test_create_order_increments_total_completed_counter(self, driver, create_user, delete_user, login_user,
                                                             counter):
        order_page = OrderPage(driver)
        order_page.open_web_page(Urls.FEED_PAGE_URL)
        counter1 = order_page.check_counter_feed_order(counter)
        order_page.open_web_page(Urls.BASE_PAGE_URL)
        order_id = order_page.make_order()
        order_page.open_web_page(Urls.FEED_PAGE_URL)
        counter2 = order_page.check_counter_feed_order(counter)
        assert counter1 < counter2

    @allure.title("Номер заказа появляется в процессе после размещения")
    @allure.description("Создает новый заказ и проверяет, что его номер появился в активных заказах, но не в завершенных.")
    def test_order_number_appears_in_progress_after_placement(self, driver, create_user, delete_user, login_user):
        order_page = OrderPage(driver)
        order_page.open_web_page(Urls.BASE_PAGE_URL)
        order_id = order_page.make_order()
        order_page.click_order_feed_and_wait()
        order_page.wait_for_active_orders_count()
        orders_in_process = order_page.get_active_orders_count()
        orders_complete = order_page.get_complete_orders_count()
        assert f"{order_id}" in orders_in_process and f"{order_id}" not in orders_complete
