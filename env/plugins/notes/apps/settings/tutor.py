from .common import *

SECRET_KEY = "hWXMS4W0re9wWKDcxzXHh2kq"
ALLOWED_HOSTS = [
    "notes",
    "notes.local.overhang.io",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "mysql",
        "PORT": 3306,
        "NAME": "notes",
        "USER": "notes",
        "PASSWORD": "irkCb2zd",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

CLIENT_ID = "notes"
CLIENT_SECRET = "NmYxtr1MIweEQhGngg8TBUra"

ELASTICSEARCH_DSL = {'default': {'hosts': 'elasticsearch:9200'}}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}

ES_DISABLED = True
