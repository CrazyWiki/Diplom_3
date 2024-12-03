import allure
from pages.base_page import BasePage
from locators.main_page_locators import ManePageLocators as MP_locators
import data.data as data



class MainPage(BasePage):
    @allure.title("Клик на любой ингредиент")
    @allure.description("Кликает на любой доступный ингредиент на странице")
    def click_any_ingridient(self):
        self.wait_until_element_is_clickable(MP_locators.BUN_INGREDIENT)
        self.click_element(MP_locators.BUN_INGREDIENT)

    @allure.title("Получение количества ингредиентов")
    @allure.description("Возвращает количество ингредиентов на странице")
    def get_ingredient_count_value(self):
        counter = self.get_text_of_element(MP_locators.INGREDIENT_COUNTER)
        return int(counter)

    @allure.title("Проверка появления описания ингредиента")
    @allure.description("Проверяет, что описание ингредиента появляется после клика на него")
    def check_description_appearence(self):
        self.wait_until_element_is_visible(MP_locators.INGREDIENT_DETAILS)
        text = self.get_text_of_element(MP_locators.INGREDIENT_DETAILS)
        return text

    @allure.title("Закрытие всплывающего окна")
    @allure.description("Закрывает всплывающее окно на странице")
    def close_popup_window(self): # туту поменять
        self.driver.find_element(*MP_locators.CROSS_BUTTON).click()

    @allure.title("Добавление начинки в заказ")
    @allure.description("Перетаскивает начинку в корзину заказа")
    def add_filling_to_order(self):
        self.wait_until_element_is_clickable(MP_locators.BUN_INGREDIENT)
        self.drag_and_drop_on_element(MP_locators.BUN_INGREDIENT,MP_locators.BURGER_CONSTRUCTOR_BASKET)

    @allure.title("Клик на кнопку 'Сделать заказ'")
    @allure.description("Кликает на кнопку 'Сделать заказ'")
    def click_order_button(self):
        self.move_to_element(MP_locators.CREATE_ORDER_BUTTON)
        self.click_element(MP_locators.CREATE_ORDER_BUTTON)

    @allure.title("Получение идентификатора заказа")
    @allure.description("Возвращает идентификатор созданного заказа")
    def get_order_id(self):
        self.wait_until_element_is_visible(MP_locators.ORDER_IDENTIFICATE)
        id = self.get_text_of_element(MP_locators.ORDER_ID)
        while id == data.ORDER_ID_BY_DEFAULT:
            id = self.get_text_of_element(MP_locators.ORDER_ID)
        return id








