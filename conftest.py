import pytest
from playwright.sync_api import sync_playwright
import json
import os
import pytest
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev"
    )


@pytest.fixture(scope="session")
def config(request):
    env_name = request.config.getoption("--env")

    load_dotenv(f"config/{env_name}.env")

    return {
        "base_url": os.getenv("BASE_URL"),
        "token": os.getenv("TOKEN")
    }


@pytest.fixture
def api_context(playwright, config):
    context = playwright.request.new_context(
        base_url=config["base_url"],
        extra_http_headers={
            "Authorization": f"Bearer {config['token']}",
            "Content-Type": "application/json"
        }
    )

    yield context
    context.dispose()


@pytest.fixture
def page(playwright:sync_playwright):
    
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    yield page

    browser.close()


@pytest.fixture
def data():
    
    with open("data/test.json") as f:
        data=json.load(f)

    return data





