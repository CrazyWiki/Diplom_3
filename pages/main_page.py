import allure
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.main_page_locators import ManePageLocators as MP_locators
from locators.base_page_locators import BasePageLocators as BP_locators
import data.data as data



class MainPage(BasePage):
    @allure.step("Клик на любой ингредиент")
    def click_any_ingridient(self):
        self.wait_until_element_is_clickable(MP_locators.BUN_INGREDIENT)
        self.click_element(MP_locators.BUN_INGREDIENT)

    @allure.step("Получение количества ингредиентов")
    def get_ingredient_count_value(self):
        counter = self.get_text_of_element(MP_locators.INGREDIENT_COUNTER)
        return int(counter)

    @allure.step("Проверка появления описания ингредиента")
    def check_description_appearence(self):
        self.wait_until_element_is_visible(MP_locators.INGREDIENT_DETAILS)
        text = self.get_text_of_element(MP_locators.INGREDIENT_DETAILS)
        return text

    @allure.step("Закрытие всплывающего окна")
    def close_popup_window(self):
        self.driver.find_element(*MP_locators.CROSS_BUTTON).click()

    @allure.step("Добавление начинки в заказ")
    def add_filling_to_order(self):
        self.wait_until_element_is_clickable(MP_locators.BUN_INGREDIENT)
        self.drag_and_drop_on_element(MP_locators.BUN_INGREDIENT,MP_locators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step("Клик на кнопку 'Сделать заказ'")
    def click_order_button(self):
        self.move_to_element(MP_locators.CREATE_ORDER_BUTTON)
        self.click_element(MP_locators.CREATE_ORDER_BUTTON)

    @allure.step("Получение идентификатора заказа")
    def get_order_id(self):
        self.wait_until_element_is_visible(MP_locators.ORDER_IDENTIFICATE)
        id = self.get_text_of_element(MP_locators.ORDER_ID)
        while id == data.ORDER_ID_BY_DEFAULT:
            id = self.get_text_of_element(MP_locators.ORDER_ID)
        return id

    @allure.step("Проверяет, что указанный элемент невидим на странице в течение заданного времени")
    def check_invisibility_of_element_MP_ingredients_details(self):
        return self.check_invisibility_of_element(element=MP_locators.INGREDIENT_DETAILS_IN_POPUP)

    @allure.step("Проверка видимости кнопки создания заказа")
    def is_create_order_button_visible(self):
        return self.wait_until_element_is_visible_return(MP_locators.CREATE_ORDER_BUTTON)







