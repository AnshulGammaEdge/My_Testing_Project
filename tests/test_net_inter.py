from playwright.sync_api import expect

def test_mock_users_api(page):

    # API intercept hone par ye function chalega
    def mock_users(route):

        # Fake response return kar rahe hain
        route.fulfill(
            status=200,
            content_type="application/json",
            json=[
                {
                    "id": 1,
                    "name": "Amit",
                    "email": "anshul@test.com",
                    "gender": "male",
                    "status": "active"
                },
                {
                    "id": 2,
                    "name": "Rahul",
                    "email": "rahul@test.com",
                    "gender": "male",
                    "status": "active"
                }
            ]
        )

    # Actual API ko intercept karo
    page.route(
        "**/public/v2/users",
        mock_users
    )

    # Website open karo jo ye API call karti ho
    page.goto("https://gorest.co.in/")


    # API call directly trigger karne ke liye
    response = page.evaluate("""
        async () => {
            const res = await fetch('https://gorest.co.in/public/v2/users');
            return await res.json();
        }
    """)

    print(response)

    assert response[0]["name"] == "Amit"
    assert response[1]["name"] == "Rahul"