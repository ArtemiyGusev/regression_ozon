import pytest
from dotenv import load_dotenv


@pytest.fixture(autouse=True, scope='session')
def environment():
    load_dotenv()
