from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    LINK_RECOVERY_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
    INPUT_EMAIL_FIELD = (By.NAME, "name")
    BUTTON_RECOVERY_PASSWORD = (By.XPATH, ".//button[text()='Восстановить']")
    RECOVERY_PASSWORD_LABEL = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    INPUT_ICON = (By.CLASS_NAME, "input__icon")
    INPUT_PASSWORD_STATUS = (By.CLASS_NAME, "input_status_active")
    BUTTON_SAVE_NEW_PASSWORD=(By.XPATH, "//button[text()='Сохранить']")