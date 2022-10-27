from voluptuous import Schema, ALLOW_EXTRA
from pytest_voluptuous import S
from base_page.helper.requests_helper import reqres


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
    response = reqres().get("api/users?page=2")
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
    response = reqres().post("api/users", params=body)
    assert response.status_code == 201
    assert S(schema) == response.json()


def test_register_user():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "citysl3icka"
    }
    response_reg = reqres().post("api/register", data=body)
    assert response_reg.status_code == 200
    response_login = reqres().post("api/login", data=body)
    assert response_login.json()['token'] == response_reg.json()['token']


def test_delete_user():
    response = reqres().delete("api/users/7")
    assert response.status_code == 204
