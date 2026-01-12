"""Unit tests for the IloveimgAuthManager class in the iloveimg module."""

import pytest
from pytest_mock import MockerFixture

from iloveimg.exceptions.auth_exception import AuthException
from iloveimg.iloveimg_api import Iloveimg

# pylint: disable=missing-function-docstring


class IloveimgAuthManager:
    """
    Class that manages authentication and credential handling for iLoveIMG,
    using the Iloveimg class internally.
    """

    def __init__(self, public_key: str | None = None, secret_key: str | None = None):
        # Always provide a non-empty secret_key for testing purposes if not given
        public_key = public_key or "dummy_key"
        secret_key = secret_key or "dummy_secret"
        self._iloveimg = Iloveimg(public_key=public_key, secret_key=secret_key)

    def set_credentials(
        self,
        public_key: str | None = None,
        secret_key: str | None = None,
    ):
        self._iloveimg.set_api_keys(public_key, secret_key)  # type: ignore

    def get_token(self):
        return self._iloveimg.get_token()

    def token_actual(self):
        return self._iloveimg.auth.token

    def get_public_key(self):
        return self._iloveimg.get_public_key()

    def get_secret_key(self):
        return self._iloveimg.get_secret_key()


class TestIloveimgAuthManager:
    """
    Test the IloveimgAuthManager class.
    """

    def test_configure_credentials(self):
        manager = IloveimgAuthManager(secret_key="dummy_secret")
        manager.set_credentials("pub_key", "sec_key")
        assert manager.get_public_key() == "pub_key"
        assert manager.get_secret_key() == "sec_key"

    def test_get_token(self, mocker: MockerFixture):
        mock_request = mocker.patch("requests.request")
        mock_response = mocker.MagicMock()
        mock_response.json.return_value = {"token": "token_cache"}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        manager = IloveimgAuthManager(public_key="pub_key", secret_key="dummy_secret")
        token = manager.get_token()
        assert token == "token_cache"
        assert manager.token_actual() == "token_cache"

    def test_token_is_reusable(self, mocker: MockerFixture):
        mock_request = mocker.patch("requests.request")
        mock_response = mocker.MagicMock()
        mock_response.json.return_value = {"token": "token_cache"}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        manager = IloveimgAuthManager(public_key="pub_key", secret_key="dummy_secret")
        token1 = manager.get_token()
        token2 = manager.get_token()
        assert token1 == token2 == "token_cache"
        mock_request.assert_called_once()

    def test_invalid_credentials_raise_exception(self, mocker: MockerFixture):
        mock_request = mocker.patch("requests.request")
        mock_response = mocker.MagicMock()
        mock_response.status_code = 401
        mock_response.json.return_value = {
            "error": {
                "type": "AuthError",
                "message": "Invalid credentials",
                "code": "401",
            }
        }
        mock_request.return_value = mock_response

        manager = IloveimgAuthManager(public_key="bad", secret_key="bad")
        with pytest.raises(AuthException):
            manager.get_token()

    def test_connection_error_raises_exception(self, mocker: MockerFixture):
        mock_request = mocker.patch("requests.request")
        mock_request.side_effect = Exception("Connection error")
        manager = IloveimgAuthManager(public_key="public", secret_key="secret")
        with pytest.raises(Exception) as excinfo:
            manager.get_token()
        assert "Connection error" in str(excinfo.value)
