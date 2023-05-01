from schemas.reqres import list_shema
from pytest_voluptuous import S


def test_single_user_not_found(reqres):
    url = 'users/23'
    response = reqres.get(url)
    assert response.status_code == 404


def test_list_resourse_schema(reqres):
    url = 'unknown'
    response = reqres.get(url)
    assert S(list_shema) == response.json()


def test_list_resourse_len(reqres):
    url = 'unknown'
    response = reqres.get(url)
    data_len = len(response.json()["data"])
    per_page = response.json()["per_page"]
    assert data_len == per_page == 6


def test_create(reqres):
    url = 'users'
    response = reqres.post(url, {
        "name": "morpheus",
        "job": "leader"
    })
    assert response.status_code == 201


def test_update(reqres):
    url = 'users/2'
    response = reqres.put(url, {
        "name": "morpheus",
        "job": "zion resident"
    })
    assert response.status_code == 200


def test_register_successful(reqres):
    url = 'register'
    response = reqres.post(url, {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    })
    id = response.json().get("id", None)
    assert id is not None


def test_list_users(reqres):
    url = 'users?page=2'
    response = reqres.get(url)
    user_first_name = response.json()["data"][0]["first_name"]
    user_last_name = response.json()["data"][0]["last_name"]
    assert user_first_name == "Michael" and user_last_name == "Lawson"


def test_single_resource_not_found(reqres):
    url = 'unknown/23'
    response = reqres.get(url)
    assert not response.json()


def test_single_user_email(reqres):
    url = 'users/2'
    response = reqres.get(url)
    assert response.json()["data"]["email"] == "janet.weaver@reqres.in"


def test_register_unsuccessful(reqres):
    url = 'register'
    response = reqres.post(url, {
        "email": "sydney@fife"
    })
    assert response.json()["error"] == "Missing password"
