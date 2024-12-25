import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data.data as data
import locators.base_page_locators as BP_locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step("Открывает веб-страницу в браузере")
    def open_web_page(self, url):
        return self.driver.get(url)


    @allure.step("Возвращает текущий URL страницы")
    def get_curent_url(self):
        return self.driver.current_url


    @allure.step("Наводит курсор на указанный элемент на странице")
    def move_to_element(self, element):
        target_element = self.driver.find_element(*element)
        ActionChains(self.driver).move_to_element(target_element).perform()

    @allure.step("Ищет элемент на странице по указанному локатору")
    def find_element(self, element):
        # Ждем, пока элемент станет доступен, затем его возвращаем
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(element))


    @allure.step("Ожидает, пока указанный элемент станет видимым на странице")
    def wait_until_element_is_visible(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element))


    @allure.step("Ожидает, пока указанный элемент станет видимым на странице и возвращает его")
    def wait_until_element_is_visible_return(self, element):
        self.wait_until_element_is_visible(element)
        return self.find_element(element)


    @allure.step("Проверяет, что указанный элемент невидим на странице в течение заданного времени")
    def check_invisibility_of_element(self, element, timeout=10, poll_frequency=0.5):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                expected_conditions.invisibility_of_element(element)
            )
            return True
        except TimeoutException:
            return False


    @allure.step("Ожидает, пока указанный элемент станет кликабельным")
    def wait_until_element_is_clickable(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))


    @allure.step("Кликает на указанный элемент на странице")
    def click_element(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        if data.DRIVER_TYPE == "chrome":
            self.driver.find_element(*element).click()
        elif data.DRIVER_TYPE == "firefox":
            WebDriverWait(self.driver, 10).until_not(
                expected_conditions.visibility_of_any_elements_located(BP_locators.BasePageLocators.MODAL_WINDOW))
            self.driver.find_element(*element).click()


    @allure.step("Возвращает текст указанного элемента")
    def get_text_of_element(self, element):
        text = self.driver.find_element(*element).text
        return text


    @allure.step("Вводит указанные данные в указанное поле на странице")
    def input_data_to_field(self, element, data):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).send_keys(data)


    @allure.step("Перетаскивает указанный элемент на другой указанный элемент")
    def drag_and_drop_on_element(self, source_locator, target_locator):
        source_element = self.driver.find_element(*source_locator)
        target_element = self.driver.find_element(*target_locator)
        if data.DRIVER_TYPE == "chrome":
            actions = ActionChains(self.driver)
            actions.drag_and_drop(source_element, target_element).perform()
        elif data.DRIVER_TYPE == "firefox":
            source = source_element
            target = target_element
            WebDriverWait(self.driver, 15).until_not(
                expected_conditions.visibility_of_any_elements_located(BP_locators.BasePageLocators.MODAL_WINDOW))
            self.driver.execute_script("""
                               var source = arguments[0];
                               var target = arguments[1];
                               var evt = document.createEvent("DragEvent");
                               evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                               source.dispatchEvent(evt);

                               evt = document.createEvent("DragEvent");
                               evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                               target.dispatchEvent(evt);

                               evt = document.createEvent("DragEvent");
                               evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                               target.dispatchEvent(evt);

                               evt = document.createEvent("DragEvent");
                               evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                               target.dispatchEvent(evt);

                               evt = document.createEvent("DragEvent");
                               evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                               source.dispatchEvent(evt);
                           """, source, target)



    @allure.step("Эта функция ищет и возвращает все элементы, соответствующие параметрам.")
    def find_all_elements(self, element):
        return WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_all_elements_located(element))


    @allure.step("Эта функция перемещает указатель мыши на элемент и кликает по нему.")
    def move_click_element(self, element):
        currency_element = self.driver.find_element(*element)
        actions = ActionChains(self.driver)
        actions.move_to_element(currency_element).click().perform()


    @allure.step("Эта функция ожидает видимости элементов и возвращает список найденных элементов.")
    def find_elements_with_wait(self, element):
        if data.DRIVER_TYPE == "firefox":
            WebDriverWait(self.driver, 15).until_not(
                expected_conditions.visibility_of_any_elements_located(BP_locators.BasePageLocators.MODAL_WINDOW))
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element))
        return self.driver.find_elements(*element)


    @allure.step("Эта функция ожидает видимости элемента и возвращает его.")
    def find_element_with_wait(self, element):
        if data.DRIVER_TYPE == "firefox":
            WebDriverWait(self.driver, 15).until_not(
                expected_conditions.visibility_of_any_elements_located(BP_locators.BasePageLocators.MODAL_WINDOW))
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element))
        return self.driver.find_element(*element)

    @allure.step("Клик по ссылке конструктора и ожидание")
    def click_constructor_link_and_wait(self):
        self.click_element(BP_locators.BasePageLocators.CONSTRUCTOR_LINK)
        self.wait_until_element_is_clickable(BP_locators.BasePageLocators.CONSTRUCTOR_LINK)

    @allure.step("Клик по ссылке ленты заказов и ожидание")
    def click_order_feed_and_wait(self):
        self.click_element(BP_locators.BasePageLocators.ORDER_FEED_LINK)
        self.wait_until_element_is_clickable(BP_locators.BasePageLocators.ORDER_FEED_LINK)

    @allure.step("Ожидание, пока значение не станет не нулевым")
    def wait_for_digit_to_be_non_zero(self,element):
        WebDriverWait(self.driver, 10).until(lambda driver: self._text_is_non_zero(element))

    @allure.step("Проверка, что текст элемента не равен нулю")
    def _text_is_non_zero(self, element):
        text_value = self.get_text_of_element(element)
        return text_value != "0"