import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.PageObject import PageObject


class ContactUsPage(PageObject):
    # Locators:
    url = 'https://magento.softwaretestingboard.com/contact/'
    name_text = 'name'
    email_text = 'email'
    phone_number_text = 'telephone'
    Whats_on_your_mind_text = 'comment'
    button_submit = "action submit primary"
    message_sucess = 'message-success success message'

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.open_contact_us_page()

    def open_contact_us_page(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='contact']").click()
        #self.driver.get(self.url)

    def set_name(self, name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.name_text)))
        self.driver.find_element(By.ID, self.name_text).send_keys(name)

    def set_email(self, email):
        self.driver.find_element(By.ID, self.email_text).send_keys(email)

    def set_phone_number(self, phone_number):
        self.driver.find_element(By.ID, self.phone_number_text).send_keys(phone_number)

    def set_comment(self, comment):
        self.driver.find_element(By.ID, self.Whats_on_your_mind_text).send_keys(comment)

    def click_button_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "#contact-form button").click()

    def confirm_message_sucess(self):
        msg = "Thanks for contacting us with your comments and questions. We'll respond to you very soon."
        return self.driver.find_element(By.CSS_SELECTOR, "[class='message-success success message'] div").text == msg
