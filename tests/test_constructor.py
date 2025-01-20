from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import MainPageLocators
 
class TestConstructor:
    # Проверка переключения на раздел 'Булки'
    def test_switch_to_buns(self, driver):
        # Клик по вкладке "Соусы" (чтобы потом проверить переключение на булки)
        sauces_tab = driver.find_element(*MainPageLocators.SAUCES_TAB)
        sauces_tab.click()

        # Клик по вкладке "Булки"
        buns_tab = driver.find_element(*MainPageLocators.BUNS_TAB)
        buns_tab.click()

        # Проверка, что вкладка "Булки" активна
        buns_tab = driver.find_element(*MainPageLocators.BUNS_TAB)

        assert "current" in buns_tab.get_attribute("class")

    # Проверка переключения на раздел 'Соусы'
    def test_switch_to_sauces(self, driver):
        # Клик по вкладке "Соусы"
        sauces_tab = driver.find_element(*MainPageLocators.SAUCES_TAB)
        sauces_tab.click()

        # Проверка, что вкладка "Соусы" активна
        assert "current"  in sauces_tab.get_attribute("class")

    # Проверка переключения на раздел 'Начинки'
    def test_switch_to_fillings(self, driver):
        # Клик по вкладке "Начинки"
        fillings_tab = driver.find_element(*MainPageLocators.FILLINGS_TAB)
        fillings_tab.click()

        # Проверка, что вкладка "Начинки" активна
        assert "current" in fillings_tab.get_attribute("class")
