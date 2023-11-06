from os import getenv

JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")
ALGORITHM = getenv("ALGORITHM", "HS256")
