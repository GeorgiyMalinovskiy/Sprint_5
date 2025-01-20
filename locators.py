from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Секции конструктора
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/..")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/..")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/..")
 
class LoginPageLocators:
    # Поля формы входа
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Ссылки на другие формы
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
 
class RegisterPageLocators:
    # Поля формы регистрации
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Сообщения об ошибках
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")
 
class ProfilePageLocators:
    # Кнопки в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
