from selenium.webdriver.common.by import By


class OrderPageLocators:
    TOTAL_ORDERS_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDERS_SUMMARY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ACTIVE_ORDERS_COUNT_2 = (By.CLASS_NAME, 'OrderFeed_orderList__cBvyi')
    ACTIVE_ORDERS_COUNT = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")
    ORDERS_LIST_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')
    ORDER_COMPOSITION = (By.XPATH, '//p[text()="Cостав"]')
    ORDERS_LIST_NUMBER = (By.CLASS_NAME, 'text_type_digits-default')
    ORDER_LINK_IN_FEED = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, 'История заказов')
    ALL_ORDERS_IN_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, 'text_type_digits-default')]")
    ALL_FEED_ORDERS = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                 "text_type_digits-default']")
