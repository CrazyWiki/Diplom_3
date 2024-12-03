class Urls:
    BASE_PAGE_URL = 'https://stellarburgers.nomoreparties.site/'
    LOGIN_PAGE_URL = f'{BASE_PAGE_URL}login'
    PROFILE_PAGE_URL = f'{BASE_PAGE_URL}account/profile'
    ORDER_HISTORY_PAGE_URL = f'{BASE_PAGE_URL}account/order-history'
    REGISTER_PAGE_URL = f'{BASE_PAGE_URL}register'
    RESTORE_PASSWORD_PAGE_URL = f'{BASE_PAGE_URL}forgot-password'
    RESET_PASSWORD_PAGE_URL = f'{BASE_PAGE_URL}reset-password'
    FEED_PAGE_URL = f'{BASE_PAGE_URL}feed'

    API_USER_CREATE = "/api/auth/register"
    API_USER_DELETE = "/api/auth/user"