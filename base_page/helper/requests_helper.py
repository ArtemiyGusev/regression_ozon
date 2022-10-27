import logging

import allure
from requests import Session
import curlify
import os


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        with allure.step(f'{method} {url}'):
            response = super().request(method, url=f'{self.base_url}{url}', **kwargs)
            msg = curlify.to_curl(response.request)
            logging.info(f' {response.status_code} {msg}')
            allure.attach(
                body=msg.encode('utf-8'),
                name=f'Request {method} {response.status_code}',
                attachment_type=allure.attachment_type.TEXT,
                extension='txt')
        return response


def reqres() -> BaseSession:
    reqres_url = os.getenv('reqres')
    return BaseSession(base_url=reqres_url)
