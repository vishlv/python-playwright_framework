import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    BASE_URL = os.getenv('BASE_URL', 'https://opensource-demo.orangehrmlive.com/')
    BROWSER = os.getenv('BROWSER', 'chromium')
    HEADLESS = os.getenv('HEADLESS', 'True')
    TIMEOUT = int(os.getenv('TIMEOUT', '15000'))

config = Config()