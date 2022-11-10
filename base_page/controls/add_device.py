from base_page.api_controls.am_bearer_authenticated import AmBearerAuthenticated
from base_page.helper.acceptance_test_modul import scroll_click
from base_page.helper.requests_helper import myglo


def add_device_click(device):
    scroll_click(device)


def add_device_api(device, email='dfgdr33drgdr@test.ru', password='Test20202020]', qty=1):
    body = {
        "cartItem":
            {
                "sku": device,
                "qty": qty
            }
    }
    response = myglo().post("rest/ru_ru/V1/carts/mine/items", json=body, auth=AmBearerAuthenticated(email, password))
    assert response.status_code == 200


def delete_all_device_api(email='dfgdr33drgdr@test.ru', password='Test20202020]'):
    devices = myglo().get("rest/ru_ru/V1/carts/mine/items/",
                          auth=AmBearerAuthenticated(email, password))
    for device in devices.json():
        response = myglo().delete("rest/ru_ru/V1/carts/mine/items/" + str(device['item_id']),
                                  auth=AmBearerAuthenticated(email, password))
        assert response.status_code == 200
