import pytest
from selenium import webdriver
import requests
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data.data
from faker import Faker
from data.urls import Urls
from locators.login_page_locators import LoginPageLocators as LP_locators
from locators.base_page_locators import BasePageLocators as BP_locators


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
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
    driver.get(f"{Urls.LOGIN_PAGE_URL}")
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LP_locators.EMAIL_FIELD))
    driver.find_element(*LP_locators.EMAIL_FIELD).send_keys(create_user[0])
    driver.find_element(*LP_locators.PASSWORD_FIELD).send_keys(create_user[1])
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LP_locators.LOGIN_BUTTON))
    if data.data.DRIVER_TYPE == "chrome":
        driver.find_element(*LP_locators.LOGIN_BUTTON).click()
    elif data.data.DRIVER_TYPE == "firefox":
        WebDriverWait(driver, 10).until_not(
            expected_conditions.visibility_of_any_elements_located(BP_locators.MODAL_WINDOW))
        driver.find_element(*LP_locators.LOGIN_BUTTON).click()
    return driver


