import curlify
import logging
from allure import step
from requests import Session


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        with step(f'Вызов {method} метода {url}'):
            response = super().request(method, url=f'{self.base_url}{url}', **kwargs)
            content_type = response.headers.get("content-type", None)

            logging.info(f"status_code:{response.status_code}, {curlify.to_curl(response.request)}")
            if not content_type:
                raise BaseException
            elif "text" in content_type:
                logging.info(response.text)
            elif "json" in content_type:
                logging.info(response.json())

        return response
