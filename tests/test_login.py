import pytest
import respx
from httpx import Response
from src.termoweb import Termoweb

@respx.mock
def test_login_success():
    mock_email = "user@example.com"
    mock_password = "securepassword"
    mock_token = "mocked_access_token"

    respx.post("https://control.termoweb.net/client/token").mock(

        return_value=Response(200, json={"access_token": mock_token})
    )

    client = Termoweb(mock_email, mock_password)
    client.login()
    assert client.userToken == mock_token

@respx.mock
def test_login_failure():
    respx.post("https://control.termoweb.net/client/token").mock(
        return_value=Response(401, json={})
    )

    client = Termoweb("user@example.com", "wrongpassword")

    with pytest.raises(Exception) as excinfo:
        client.login()

    assert "Login failed: 401" in str(excinfo.value)
