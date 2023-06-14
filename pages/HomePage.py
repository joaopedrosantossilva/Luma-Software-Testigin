from pages.PageObject import PageObject

class HomePage(PageObject):
    # Locators
    url = 'https://magento.softwaretestingboard.com/'


    def __init__(self, browser):
        super().__init__(browser=browser)
        self.open_home_page()

    def open_home_page(self):
        self.driver.get(self.url)











