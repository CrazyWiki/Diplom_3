import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as OP_locators
from locators.base_page_locators import BasePageLocators as BP_locators
from locators.main_page_locators import ManePageLocators as MP_locators
import time
import data.data as data


class OrderPage(BasePage):
    @allure.title("Клик по кнопке заказа")
    @allure.description("Нажимает на кнопку заказа в ленте.")
    def click_order_button(self):
        self.click_element(OP_locators.ORDER_LINK_IN_FEED)

    @allure.title("Проверка деталей заказа")
    @allure.description("Ожидает появления деталей заказа и проверяет, отображаются ли они.")
    def check_order_details(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(OP_locators.ORDER_COMPOSITION))
        details = self.driver.find_element(*OP_locators.ORDER_COMPOSITION)
        print(details)
        return details.is_displayed()

    @allure.title("Проверка идентификатора заказа")
    @allure.description("Проверяет, совпадает ли идентификатор заказа с одним из найденных элементов.")
    def check_order_id(self, id, element):
        all_elements = self.driver.find_all_elements(element)
        for each_element in all_elements:
            if id == each_element.text:
                return True
            return True


    def get_order_of_user(self, order_number):
        order = f'#0{order_number}'
        return order



    @allure.title("Добавление начинки в заказ")
    @allure.description("Перетаскивает начинку в корзину заказа")
    def add_filling_to_order(self):
        self.wait_until_element_is_clickable(MP_locators.BUN_INGREDIENT)
        self.drag_and_drop_on_element(MP_locators.BUN_INGREDIENT, MP_locators.BURGER_CONSTRUCTOR_BASKET)

    @allure.title("Получение идентификатора заказа")
    @allure.description("Возвращает идентификатор созданного заказа")
    def get_order_id(self):
        self.wait_until_element_is_visible(MP_locators.ORDER_IDENTIFICATE)
        id = self.get_text_of_element(MP_locators.ORDER_ID)
        while id == data.ORDER_ID_BY_DEFAULT:
            id = self.get_text_of_element(MP_locators.ORDER_ID)
        return id

    @allure.title("Создание заказа")
    @allure.description("Создает новый заказ, добавляя начинку и нажимая на кнопку создания заказа.")
    def make_order(self):
        self.add_filling_to_order()
        time.sleep(2)
        self.click_element(MP_locators.CREATE_ORDER_BUTTON)
        order_number = self.get_order_id()
        id = self.get_order_of_user(order_number)
        self.move_click_element(MP_locators.CROSS_BUTTON)
        return id

    @allure.title("Получение идентификатора заказа в ленте")
    @allure.description("Проверяет, присутствует ли заказ с определенным идентификатором в ленте.")
    def get_order_id_in_feed(self, order_id):
        # self.click_close_modal_order()
        time.sleep(2)
        self.click_element(BP_locators.ORDER_FEED_LINK)
        time.sleep(2)
        all_elements_feed_order = self.driver.find_elements(*OP_locators.ORDERS_LIST_NUMBER)
        all_elements_feed_order_text = [element.text for element in all_elements_feed_order if
                                         element.text.startswith("#")]
        if order_id in all_elements_feed_order_text:
            return True
        else:
            return False

    @allure.title("Проверка счетчика заказов в ленте")
    @allure.description("Находит элемент счетчика заказов в ленте и возвращает его значение как целое число.")
    def check_counter_feed_order(self,counter_locator):
        counter=self.find_element_with_wait(counter_locator).text
        return int(counter)


