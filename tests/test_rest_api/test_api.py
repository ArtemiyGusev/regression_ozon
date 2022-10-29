import random

from voluptuous import Schema, ALLOW_EXTRA
from pytest_voluptuous import S
from base_page.helper.requests_helper import myglo
from base_page.helper.module_helper import rand_string, rand_int
from base_page.api_controls.am_bearer_authenticated import AmBearerAuthenticated


def test_get_users_page():
    schema = Schema({
        'page': int,
        'per_page': int,
        'total': int,
        'data': object,
        'support': {'text': str}

    },
        extra=ALLOW_EXTRA,
    )
    response = myglo().get("api/users?page=2")
    assert response.status_code == 200
    assert S(schema) == response.json()
    assert response.json()['page'] == 2


def test_post_create_users():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    schema = Schema({
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    })
    response = myglo().post("api/users", params=body)
    assert response.status_code == 201
    assert S(schema) == response.json()


def test_register_user():
    body = {
        "customer": {
            "store_id": 2,
            "email": rand_string(13) + "@test.ru",
            "firstname": "JaneTester",
            "lastname": "DoeTester",
            "dob": "2000-01-01",
            "gender": 1,
            "custom_attributes": {
                "glo_phone_no": "+7495" + str(rand_int(1000000, 9999999))
            },
        },
        "password": "Test20202020]"
    }
    response_reg = myglo().post("rest/ru_ru/V1/customers", json=body)
    schema = Schema({
        "firstname": str,
        "lastname": str,
        "gender": int
    },
        extra=ALLOW_EXTRA,
    )
    assert S(schema) == response_reg.json()
    assert response_reg.status_code == 200

    body = {
        "username": response_reg.json()["email"],
        "password": "Test20202020]"
    }
    token = myglo().post("rest/ru_ru/V1/integration/customer/token", json=body)

    headers = {'Content-type': 'application/json'}
    body = {
        "currentPassword": "Test20202020]",
        "newPassword": "Test202020"
    }
    response_change_password = myglo().put("rest/V1/customers/me/password", json=body, headers=headers,
                                           auth=AmBearerAuthenticated(token.json()))
    assert response_change_password.json() == True
    assert response_change_password.status_code == 200


def test_delete_user():
    # response = myglo().delete("api/users/7")
    # assert response.status_code == 204
    rand = ''.join(
        [random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(12)])
    print(rand)
