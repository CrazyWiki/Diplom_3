from selenium.webdriver.common.by import By

class Locators:
    # Заголовок страницы
    PAGE_TITLE = (By.TAG_NAME, 'h1')

    # Линк на конструктор
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    # Линк на ленту заказов
    FEED_LINK = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")

    # Линк на личный кабинет
    ACCOUNT_LINK = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")

    # Раздел ингредиентов
    INGREDIENTS_SECTION = (By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")

    # Заголовок для "Соберите бургер"
    BURGER_HEADER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")

    # Таб для булок
    BUN_TAB = (By.XPATH, "//span[text()='Булки']")

    # Таб для соусов
    SAUCE_TAB = (By.XPATH, "//span[text()='Соусы']")

    # Таб для начинок
    FILLING_TAB = (By.XPATH, "//span[text()='Начинки']")

    # Ингредиенты (пример для первого ингредиента)
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[1]")

    # Кнопка "Войти в аккаунт"
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")

    # Сообщение об успешном заказе
    SUCCESS_MESSAGE = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq' and text()='9999']")
