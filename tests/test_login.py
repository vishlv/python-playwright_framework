import pytest, os
from pages.login_page import LoginPage
from utilities.config import config

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate(config.BASE_URL)
    assert login_page.perform_login("Admin", "admin123")
    assert config.BASE_URL not in page.url

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate(config.BASE_URL)
    assert login_page.perform_login("Admi", "adin123") == False
