import pytest

from utilities.config import config


@pytest.fixture(scope="session")
def base_url():
    return config.BASE_URL

    


