from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import MainPageLocators, LoginPageLocators

class TestLogin:
    # Проверка входа через кнопку 'Войти в аккаунт' на главной"
    def test_login_from_main_page(self, driver):
    
        # Клик по кнопке "Войти в аккаунт"
        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        # Заполнение формы входа
        email_input = driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)

        email_input.send_keys("17_qa_python_test@yandex.ru")
        password_input.send_keys("123456")

        # Клик по кнопке входа
        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.click()

        # Проверка успешного входа
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.CONSTRUCTOR_BUTTON))

    # Проверка входа через кнопку 'Личный кабинет'"
    def test_login_from_personal_account(self, driver):
        # Клик по кнопке "Личный кабинет"

        profile_button = driver.find_element(*MainPageLocators.PROFILE_BUTTON)
        profile_button.click()

        # Заполнение формы входа
        email_input = driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        email_input.send_keys("17_qa_python_test@yandex.ru")
        password_input.send_keys("123456")

        # Клик по кнопке входа
        submit_button =driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.click()
        
        # Проверка успешного входа
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.CONSTRUCTOR_BUTTON))

    # Проверка входа через форму регистрации
    def test_login_from_registration_page(self, driver):

        # Клик по кнопке "Личный кабинет"
        profile_button = driver.find_element(*MainPageLocators.PROFILE_BUTTON)
        profile_button.click()

        # Переход на страницу регистрации
        register_link = driver.find_element(*LoginPageLocators.REGISTER_LINK)
        register_link.click()

        # Клик по ссылке "Войти"
        login_link = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_link.click()

        # Заполнение формы входа
        email_input = driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)

        email_input.send_keys("17_qa_python_test@yandex.ru")
        password_input.send_keys("123456")

        # Клик по кнопке входа
        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.click()

        # Проверка успешного входа
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.CONSTRUCTOR_BUTTON)) 