from multiprocessing import get_logger
from playwright.sync_api import expect
# from utilities.config import config

class BasePage:

    def __init__(self, page):
        self.page = page
        # self.logger = get_logger(self.__class__.__name__)
        # self.timeout = config.TIMEOUT

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, selector):
        self.page.locator(selector).click()

    def fill(self, selector, text):
        self.page.locator(selector).fill(text)
    
    def fetch_text(self, selector):
        return self.page.locator(selector).inner_text()
    
    def select_option(self, selector, option):
        self.page.locator(selector).select_option(option)
    
    def is_visible(self, selector):
        return expect(self.page.locator(selector)).to_be_visible()
    

        