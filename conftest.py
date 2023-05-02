import os
from utils.helper import BaseSession
from dotenv import load_dotenv
import pytest

load_dotenv()

REQRES_URL = os.getenv('reqres_base_url')


@pytest.fixture(scope="session")
def reqres():
    reqres_session = BaseSession(base_url=REQRES_URL)
    return reqres_session
