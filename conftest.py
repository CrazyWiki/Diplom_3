import pytest
from selenium import webdriver
import requests
import allure

import data.data
from faker import Faker
from data.urls import Urls
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request): #request позволяет получить текущее значение параметра в фикстуре
    if request.param == 'chrome':
        data.data.DRIVER_TYPE="chrome"
        driver_instance = webdriver.Chrome()
    elif request.param == 'firefox':
        driver_instance= webdriver.Firefox()
        data.data.DRIVER_TYPE = "firefox"
    yield driver_instance
    driver_instance.quit()

@pytest.fixture
def create_user():
    faker = Faker()
    random_data = {
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.name()
    }

    response = requests.post(f"{Urls.BASE_PAGE_URL}{Urls.API_USER_CREATE}", json=random_data).json()
    return random_data['email'], random_data['password'], random_data['name'], response


@pytest.fixture
@allure.title("Удаляю созданного пользователя")
def delete_user(create_user):
    access_token = create_user[3]['accessToken']
    yield
    requests.delete(f"{Urls.BASE_PAGE_URL}{Urls.API_USER_DELETE}", headers={"Authorization": f"{access_token}"})

@pytest.fixture
def login_user(driver, create_user):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)

    driver.get(f"{Urls.LOGIN_PAGE_URL}")
    login_page.enter_email(create_user[0])
    login_page.enter_password(create_user[1])
    login_page.click_login_button()

    assert main_page.is_create_order_button_visible()



