from selenium.webdriver.common.by import By
class LoginPageLocators:
    TEXT_ENTER = (By.XPATH, ".//h2[text()='Вход']")
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//div/main/div/form/button")