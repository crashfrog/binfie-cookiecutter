import pytest


@pytest.fixture
def base_context():
    return {
        "full_name": "John Doe",
        "email": "jondoe@example.com",
        "github_username": "johndoe",
        "project_name": "My Cool Project",
        "__name_check": False,
    }
