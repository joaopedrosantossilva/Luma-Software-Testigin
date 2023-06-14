from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class LoginPage(PageObject):

    # Locators
    url = 'https://magento.softwaretestingboard.com/customer/account/login'
    id_login_btn = 'send2'
    name_email = 'email'
    name_password = 'pass'

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.open_login_page()

    def open_login_page(self):
        self.driver.get(self.url)

    def click_login_btn(self):
        self.driver.find_element(By.ID, self.id_login_btn).click()

    def is_url_login(self):
        return self.driver.current_url == self.url

    def efetuar_login(self, username='teste123@teste.com', password='Teste123'):
        self.driver.find_element(By.ID, self.name_email).send_keys(username)
        self.driver.find_element(By.ID, self.name_password).send_keys(password)
        self.click_login_btn()

