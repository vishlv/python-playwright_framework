
class LoginPageLocators:
    USERNAME_FIELD =  "input[name=username]"
    PASSWORD_FIELD = "input[name=password]"
    LOGIN_BTN = "button[type=submit]"

    ERROR_MESSAGE_LOCATOR = "//span[text()='Required']"
    ERROR_MESSAGE_FOR_INVALID_CREDS = "//p[text()='Invalid credentials']"