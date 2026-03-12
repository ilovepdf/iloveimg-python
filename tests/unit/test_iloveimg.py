"""Unit tests for the Iloveimg class in the iloveimg module."""

import pytest
from pytest_mock import MockerFixture

from iloveimg.exceptions.auth_exception import AuthException
from iloveimg.iloveimg_api import Iloveimg

ERROR_500 = {
    "error": {
        "type": "ServerError",
        "message": "Something on our end went wrong, probably we are not catching "
        "some exception we should catch! We are logging this and we will "
        "fix it.",
        "code": "500",
    }
}


class TestIloveImgAuth:
    """Unit tests for the IloveimgAuth class in the iloveimg module."""

    def test_set_api_keys_stores_credentials(self):
        iloveimg = Iloveimg(
            public_key="dummy_public_key", secret_key="dummy_secret_key"
        )
        iloveimg.set_api_keys("my_public_key", "my_secret_key")
        assert iloveimg.get_public_key() == "my_public_key"
        assert iloveimg.get_secret_key() == "my_secret_key"

    def test_get_token_success(self, mocker: MockerFixture):
        mock_request = mocker.patch("requests.request")
        mock_response = mocker.MagicMock()
        mock_response.json.return_value = {"token": "token_abc"}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        iloveimg = Iloveimg(public_key="public_key", secret_key="dummy_secret")
        token = iloveimg.get_token()
        assert token == "token_abc"

    def test_get_token_invalid_credentials_raises_auth_exception(
        self, mocker: MockerFixture
    ):
        mock_request = mocker.patch("requests.request")
        mock_response = mocker.MagicMock()
        mock_response.status_code = 401
        mock_response.json.return_value = ERROR_500
        mock_request.return_value = mock_response

        iloveimg = Iloveimg(public_key="bad", secret_key="dummy_secret")
        # We force the method to raise AuthException
        with pytest.raises(AuthException):
            iloveimg.send_request(
                "get", "auth", {"json": {"public_key": "bad"}}, start=True
            )

    def test_get_token_connection_error(self, mocker: MockerFixture):
        # Simulates a requests connection error
        mock_request = mocker.patch("requests.request")
        mock_request.side_effect = Exception("Connection error")
        iloveimg = Iloveimg(public_key="public", secret_key="secret")
        with pytest.raises(Exception) as excinfo:
            iloveimg.get_token()
        assert "Connection error" in str(excinfo.value)

    def test_token_is_cached_and_not_requested_twice(self, mocker: MockerFixture):
        mock_request = mocker.patch("requests.request")
        mock_response = mocker.MagicMock()
        mock_response.json.return_value = {"token": "cached_token"}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        iloveimg = Iloveimg(public_key="public", secret_key="secret")
        token1 = iloveimg.get_token()
        token2 = iloveimg.get_token()
        assert token1 == token2 == "cached_token"
        mock_request.assert_called_once()

    def test_get_token_missing_token_in_response_raises_keyerror(
        self, mocker: MockerFixture
    ):
        mock_request = mocker.patch("requests.request")
        mock_response = mocker.MagicMock()
        mock_response.json.return_value = {}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        iloveimg = Iloveimg(public_key="public", secret_key="secret")
        with pytest.raises(KeyError):
            iloveimg.get_token()
