import os
from collections import namedtuple

BOT_TOKEN = "secret"
OWM_APPID = "secret"

DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgres://secret@localhost:5432/postgres"
)
REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["travelagent.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

Locale = namedtuple("Locale", ["lang_code", "flag", "name"])
LOCALES = {
    "en": Locale("en", ":United_States:", "English"),
    "ru": Locale("ru", ":Russia:", "Русский"),
}
DEFAULT_LOCALE = LOCALES["en"]
