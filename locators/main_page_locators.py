from selenium.webdriver.common.by import By

class ManePageLocators:


    LOGIN_BUTTON=(By.XPATH,".//button[text()='Войти в аккаунт']")
    TITLE_TEXT=(By.XPATH,".//h1[text()='Соберите бургер']")
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    BUN_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')

    SAUSE_BUTTON = (By.XPATH, ".//span[text()='Соусы']/parent::*")
    BAN_BUTTON = (By.XPATH, ".//span[text()='Булки']/parent::*")
    FILLING_BUTTON = (By.XPATH, ".//span[text()='Начинки']/parent::*")

    H_SAUSE = (By.XPATH, ".//h2[contains(@class,'text text_type_main') and text()='Соусы']")
    H_BAN = (By.XPATH, ".//h2[contains(@class,'text text_type_main') and text()='Булки']")
    H_FILLING = (By.XPATH, ".//h2[contains(@class,'text text_type_main') and text()='Начинки']")

    INGREDIENT_FILLING_BEEF=(By.XPATH,".//img[text()='Говяжий метеорит (отбивная)']")
    INGREDIENT_BUN = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    INGREDIENT_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    CROSS_BUTTON = By.XPATH, '//button[contains(@class,"close")]'

    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')


    BURGER_CONSTRUCTOR_BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']")
    ORDER_IDENTIFICATE = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    INGREDIENT_DETAILS_IN_POPUP = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    CLOSE_MODAL_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")



