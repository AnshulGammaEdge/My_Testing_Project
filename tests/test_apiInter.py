from playwright.sync_api import sync_playwright
import json


def mock_users(route):
    fake_response = [
        {"id": 1, "name": "Anshul"},
        {"id": 2, "name": "Rahul"}
    ]

    route.fulfill(
        status=200,
        content_type="application/json",
        body=json.dumps(fake_response)
    )


def test_api_mock():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.route("https://gorest.co.in/public/v2/users", mock_users)

        page.set_content("""
        <button id="login-btn">Login</button>

        <script>
        document.getElementById("login-btn").onclick = async () => {
            const response = await fetch("https://gorest.co.in/public/v2/users");
            const data = await response.json();
            console.log(data);
        }
        </script>
        """)

        page.click("#login-btn")

        page.wait_for_timeout(3000)

        browser.close()