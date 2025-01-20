import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators

 
class TestRegistration:
    # Генерация тестового email
    def generate_test_email(self):
        return f"17_qa_python_{random.randint(1000, 9999)}@yandex.ru"

    # Проверка успешной регистрации
    def test_successful_registration(self, driver):
        # Клик по кнопке "Личный кабинет"
        profile_button = driver.find_element(*MainPageLocators.PROFILE_BUTTON)
        profile_button.click()

        # Клик по ссылке "Зарегистрироваться"
        register_link = driver.find_element(*LoginPageLocators.REGISTER_LINK)
        register_link.click()

        # Заполнение формы регистрации
        name_input = driver.find_element(*RegisterPageLocators.NAME_INPUT)
        email_input = driver.find_element(*RegisterPageLocators.EMAIL_INPUT)
        password_input = driver.find_element(*RegisterPageLocators.PASSWORD_INPUT)

        test_email = self.generate_test_email()
        name_input.send_keys("Тест Тестович")
        email_input.send_keys(test_email)
        password_input.send_keys("123456")

        # Клик по кнопке "Зарегистрироваться"
        register_button = driver.find_element(*RegisterPageLocators.REGISTER_BUTTON)
        register_button.click()

        # Проверка, что перешли на страницу входа
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON))
