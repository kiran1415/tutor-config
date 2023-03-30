from ..production import *

SECRET_KEY = "3DjuTfke29WlW5iYxJcH"
ALLOWED_HOSTS = [
    "discovery",
    "discovery.local.overhang.io"
]

PLATFORM_NAME = "My Open edX"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "discovery",
        "USER": "discovery",
        "PASSWORD": "0FuN1sei",
        "HOST": "mysql",
        "PORT": "3306",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

ELASTICSEARCH_DSL['default'].update({
    'hosts': "http://elasticsearch:9200/"
})



CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "KEY_PREFIX": "discovery",
        "LOCATION": "redis://@redis:6379/1",
    }
}

# Some openedx language codes are not standard, such as zh-cn
LANGUAGE_CODE = {
    "zh-cn": "zh-hans",
    "zh-hk": "zh-hant",
    "zh-tw": "zh-hant",
}.get("en", "en")
PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE
PARLER_LANGUAGES[1][0]["code"] = LANGUAGE_CODE
PARLER_LANGUAGES["default"]["fallbacks"] = [PARLER_DEFAULT_LANGUAGE_CODE]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp"
EMAIL_PORT = "8025"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False

# Get rid of the "local" handler
LOGGING["handlers"].pop("local")
for logger in LOGGING["loggers"].values():
    if "local" in logger["handlers"]:
        logger["handlers"].remove("local")
# Decrease verbosity of algolia logger
LOGGING["loggers"]["algoliasearch_django"] = {"level": "WARNING"}

OAUTH_API_TIMEOUT = 5

import json
JWT_AUTH["JWT_ISSUER"] = "http://local.overhang.io/oauth2"
JWT_AUTH["JWT_AUDIENCE"] = "openedx"
JWT_AUTH["JWT_SECRET_KEY"] = "bNu0FXp77dOFFjn6eygBVKAt"
# TODO assign a discovery-specific public key
JWT_AUTH["JWT_PUBLIC_SIGNING_JWK_SET"] = json.dumps(
    {
        "keys": [
            {
                "kid": "openedx",
                "kty": "RSA",
                "e": "AQAB",
                "n": "xCPURKU-XxJgJ-7IBPr5o3rpxG4UvS_NAl1LpLkdXlDz0l0CelR-yXSv3PJDeFkwEH_1YKR85CgkxZWAIwnykOz0XcYg0hXbEPn97qWVwcuOiDvOuZriKQYN8Mc9QmZKV4_dag4i4c1YATyhXqxaY_HpjDlR5Ur-4lJsKsWKXofFCfeLirQuOyFYQy3ovXrflY510HBprkVmFOGcQs0AijD6U3WYOEq-dCbIwm6z-8j4TxiDdFE4S_LHdq-LdQAlYfQIyvsosgx0Zu70b5c8kyOcZUvGUnnnnf9noH9r7KizV4DOwfpwRVlwY3PPeXXRKtTBZiA0ZX7AhB_rXuEobQ",
            }
        ]
    }
)
JWT_AUTH["JWT_ISSUERS"] = [
    {
        "ISSUER": "http://local.overhang.io/oauth2",
        "AUDIENCE": "openedx",
        "SECRET_KEY": "bNu0FXp77dOFFjn6eygBVKAt"
    }
]

EDX_DRF_EXTENSIONS = {
    'OAUTH2_USER_INFO_URL': 'http://local.overhang.io/oauth2/user_info',
}



BACKEND_SERVICE_EDX_OAUTH2_KEY = "discovery"
BACKEND_SERVICE_EDX_OAUTH2_SECRET = "5jRGYGoI"
BACKEND_SERVICE_EDX_OAUTH2_PROVIDER_URL = "http://lms:8000/oauth2"

SOCIAL_AUTH_EDX_OAUTH2_KEY = "discovery-sso"
SOCIAL_AUTH_EDX_OAUTH2_SECRET = "1mC7ICUw"
SOCIAL_AUTH_EDX_OAUTH2_ISSUER = "http://local.overhang.io"
SOCIAL_AUTH_EDX_OAUTH2_URL_ROOT = SOCIAL_AUTH_EDX_OAUTH2_ISSUER
SOCIAL_AUTH_EDX_OAUTH2_PUBLIC_URL_ROOT = SOCIAL_AUTH_EDX_OAUTH2_ISSUER
SOCIAL_AUTH_EDX_OAUTH2_LOGOUT_URL = SOCIAL_AUTH_EDX_OAUTH2_ISSUER + "/logout"

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False

