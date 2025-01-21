import pytest
from selenium import webdriver

@pytest.fixture
def driver(path):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get(f"https://stellarburgers.nomoreparties.site/{path}")

    yield driver

    driver.quit()