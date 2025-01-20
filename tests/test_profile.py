from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
 
class TestProfile:
    # Вспомогательный метод для входа в систему
    def login(self, driver):
        # Клик по кнопке "Личный кабинет"
        profile_button = driver.find_element(*MainPageLocators.PROFILE_BUTTON)
        profile_button.click()

        # Заполнение формы входа
        email_input = driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        email_input.send_keys("17_qa_python_test@yandex.ru")
        password_input.send_keys("123456")

        # Клик по кнопке входа
        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.click()

        # Ожидание загрузки страницы
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.CONSTRUCTOR_BUTTON))

    # Проверка перехода в личный кабинет
    def test_go_to_profile(self, driver):
        # Вход
        self.login(driver)

        # Клик по кнопке "Личный кабинет"
        profile_button = driver.find_element(*MainPageLocators.PROFILE_BUTTON)
        profile_button.click()

        # Проверка, что перешли в личный кабинет (видим кнопку выхода)
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))

    # Проверка перехода из личного кабинета в конструктор
    def test_go_to_constructor_from_profile(self, driver):
        # Выполняем вход и переход в личный кабинет
        self.login(driver)
        profile_button = driver.find_element(*MainPageLocators.PROFILE_BUTTON)
        profile_button.click()

        # Клик по кнопке "Конструктор"
        constructor_button = driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        # Проверка, что видим вкладку "Булки"
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.BUNS_TAB))

    # Проверка перехода из личного кабинета в конструктор по клику на лого
    def test_go_to_constructor_by_logo(self, driver):
        # Выполняем вход и переход в личный кабинет
        self.login(driver)
        profile_button = driver.find_element(*MainPageLocators.PROFILE_BUTTON)
        profile_button.click()

        # Клик по логотипу
        logo = driver.find_element(*MainPageLocators.LOGO)
        logo.click()

        # Проверка, что перешли в конструктор
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.BUNS_TAB))

    # Проверка выхода из аккаунта
    def test_logout(self, driver):
        # Выполняем вход и переход в личный кабинет
        self.login(driver)
        profile_button = driver.find_element(*MainPageLocators.PROFILE_BUTTON)
        profile_button.click()

        # Клик по кнопке выхода
        logout_button = driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON)
        logout_button.click()

        # Проверка, что вышли
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON))