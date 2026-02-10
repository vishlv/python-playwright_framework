import pytest, os
from pages.login_page import LoginPage
from utilities.config import config
from utilities.common_functions import Common_functions

test_data = Common_functions().get_test_data()


@pytest.mark.parametrize(
        "username, password, expected_result",
        [(test_data['valid_users'][0]['username'],test_data['valid_users'][0]['password'], True),
         (test_data['invalid_users'][0]['username'],test_data['invalid_users'][0]['password'], False)],
         ids=["TEST_01_Valid_creds",
              "TEST_02_Invalid_creds"])
def test_valid_login(page, username, password, expected_result):
    login_page = LoginPage(page)
    login_page.navigate(config.BASE_URL)
    result =  login_page.perform_login(username, password)
    assert result == expected_result, "Expected result do not match"



