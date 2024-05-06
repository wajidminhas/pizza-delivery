from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

DATABASE_URL_PIZZA = config("DATABASE_URL_PIZZA", cast=Secret)
