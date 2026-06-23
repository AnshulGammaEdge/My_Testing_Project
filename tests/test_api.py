import time
import pytest


def generate_email():
    timestamp = int(time.time() * 1000)
    return f"johnwick{timestamp}@gmail.com"


def test_get_api(api_context):
    response = api_context.get("/public/v2/users")

    assert response.status == 200
    print(response.json()[0]["id"])


@pytest.fixture
def create_user(api_context):
    payload = {
        "name": "Rahul",
        "email": generate_email(),
        "gender": "male",
        "status": "active"
    }

    response = api_context.post(
        "/public/v2/users",
        data=payload
    )

    assert response.status == 201

    user_data = response.json()
    print("Created User:", user_data)

    return user_data["id"]


def test_put(api_context, create_user):
    payload = {
        "name": "Rahul Updated"
    }

    response = api_context.put(
        f"/public/v2/users/{create_user}",
        data=payload
    )

    assert response.status == 200

    updated_data = response.json()
    print("Updated User:", updated_data)


def test_patch_api(api_context, create_user):
    payload = {
        "email": generate_email()
    }

    response = api_context.patch(
        f"/public/v2/users/{create_user}",
        data=payload
    )

    assert response.status == 200

    patched_data = response.json()
    print("Patched User:", patched_data)


def test_delete_api(api_context, create_user):
    response = api_context.delete(
        f"/public/v2/users/{create_user}"
    )

    assert response.status == 204
    print("User Deleted Successfully")