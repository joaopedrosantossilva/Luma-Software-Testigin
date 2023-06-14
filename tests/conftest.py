import pytest
from pages.ContactUsPage import ContactUsPage
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage

def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox", help="Set browser")

@pytest.fixture()
def choose_browser(request):
    selected_browser = request.config.getoption("--browser").lower()
    yield selected_browser

@pytest.fixture()
def open_login(choose_browser):
    login_page = LoginPage(browser=choose_browser)
    yield login_page
    login_page.close()

@pytest.fixture()
def efetuar_login(open_login):
    print("efetuar login")
    open_login.efetuar_login()
    yield open_login

@pytest.fixture()
def open_home(choose_browser):
    home_page = HomePage(browser=choose_browser)
    yield home_page