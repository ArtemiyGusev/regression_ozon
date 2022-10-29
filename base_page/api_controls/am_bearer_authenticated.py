from base_page.helper.requests_helper import myglo


class AmBearerAuthenticated:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __call__(self, r):
        body = {
           "username": self.email,
           "password": self.password
        }
        token = myglo().post("rest/ru_ru/V1/integration/customer/token", json=body)
        r.headers["authorization"] = "Bearer " + token.json()
        return r
