from pages.ContactUsPage import ContactUsPage
from faker import Faker

class Test1:
    def test_entrar_em_contato(self, open_home):
        #Data Generation
        generator = Faker()
        name = generator.unique.first_name()
        email = name+'@teste.com'
        phone_number = generator.msisdn()
        comment = generator.sentences()

        contact_us_page = ContactUsPage(driver=open_home.driver)
        contact_us_page.set_name(name)
        contact_us_page.set_email(email)
        contact_us_page.set_phone_number(phone_number)
        contact_us_page.set_comment(comment)
        contact_us_page.click_button_submit()
        assert contact_us_page.confirm_message_sucess()