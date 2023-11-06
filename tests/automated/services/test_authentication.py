from jose import jwt

from warehouse_manager.services.authentication import create_access_token, verify_token


class TestAuthenticationService:
    def setup_method(self) -> None:
        self.token_data = {"info": "test info token", "from": "Test"}

    def test_create_access_token(self) -> None:
        token = create_access_token(self.token_data)

        assert token is not None
        assert jwt.get_unverified_claims(token).get("exp") is not None
        for item in self.token_data:
            assert jwt.get_unverified_claims(token).get(item) == self.token_data.get(item)

    def test_verify_valid_access_token(self) -> None:
        token = create_access_token(self.token_data)

        assert verify_token(token) is True
