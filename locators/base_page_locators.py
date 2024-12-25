from selenium.webdriver.common.by import By


class BasePageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор' and contains(@class,'AppHeader')]/parent::*")
    ORDER_FEED_LINK = (By.XPATH, ".//p[text()='Лента Заказов' and contains(@class,'AppHeader')]")
    ACCOUNT_LINK = (By.XPATH, ".//p[text()='Личный Кабинет' and contains(@class,'AppHeader')]")
    LOGO_HEADER=(By.XPATH, ".//a//parent::*/div[contains(@class,'AppHeader_header__logo')]")

    MODAL_WINDOW_CLOSE = By.CLASS_NAME, 'Modal_modal__close_modified__3V5XS'
    MODAL_WINDOW = By.CLASS_NAME, 'Modal_modal_overlay__x2ZCr'
