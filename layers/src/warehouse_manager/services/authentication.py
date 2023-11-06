from datetime import datetime, timedelta
from typing import Any

from jose import JWTError, jwt
from pydantic import BaseModel

from warehouse_manager.configs.authentication import ALGORITHM, JWT_SECRET_KEY


class Token(BaseModel):
    access_token: str
    token_type: str


def create_access_token(data: dict[str, Any]) -> str:
    to_encode = data.copy()

    # expire time of the token
    expire = datetime.utcnow() + timedelta(minutes=10)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)

    # return the generated token
    return str(encoded_jwt)


def verify_token(token: str) -> bool:
    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM]) is not None
    except JWTError:
        return False
