# -*- coding: utf-8 -*-
import os
from cms.envs.devstack import *

LMS_BASE = "local.overhang.io:8000"
LMS_ROOT_URL = "http://" + LMS_BASE

# Authentication
SOCIAL_AUTH_EDX_OAUTH2_KEY = "cms-sso-dev"
SOCIAL_AUTH_EDX_OAUTH2_PUBLIC_URL_ROOT = LMS_ROOT_URL

FEATURES["PREVIEW_LMS_BASE"] = "preview.local.overhang.io:8000"

####### Settings common to LMS and CMS
import json
import os

from xmodule.modulestore.modulestore_settings import update_module_store_settings

# Mongodb connection parameters: simply modify `mongodb_parameters` to affect all connections to MongoDb.
mongodb_parameters = {
    "db": "openedx",
    "host": "mongodb",
    "port": 27017,
    "user": None,
    "password": None,
    # Connection/Authentication
    "ssl": False,
    "authSource": "admin",
    "replicaSet": None,
    
}
DOC_STORE_CONFIG = mongodb_parameters
CONTENTSTORE = {
    "ENGINE": "xmodule.contentstore.mongo.MongoContentStore",
    "ADDITIONAL_OPTIONS": {},
    "DOC_STORE_CONFIG": DOC_STORE_CONFIG
}
# Load module store settings from config files
update_module_store_settings(MODULESTORE, doc_store_settings=DOC_STORE_CONFIG)
DATA_DIR = "/openedx/data/modulestore"

for store in MODULESTORE["default"]["OPTIONS"]["stores"]:
   store["OPTIONS"]["fs_root"] = DATA_DIR

# Behave like memcache when it comes to connection errors
DJANGO_REDIS_IGNORE_EXCEPTIONS = True

# Elasticsearch connection parameters
ELASTIC_SEARCH_CONFIG = [{
  
  "host": "elasticsearch",
  "port": 9200,
}]

CONTACT_MAILING_ADDRESS = "My Open edX - http://local.overhang.io"

DEFAULT_FROM_EMAIL = ENV_TOKENS.get("DEFAULT_FROM_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
DEFAULT_FEEDBACK_EMAIL = ENV_TOKENS.get("DEFAULT_FEEDBACK_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
SERVER_EMAIL = ENV_TOKENS.get("SERVER_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
TECH_SUPPORT_EMAIL = ENV_TOKENS.get("TECH_SUPPORT_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
CONTACT_EMAIL = ENV_TOKENS.get("CONTACT_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
BUGS_EMAIL = ENV_TOKENS.get("BUGS_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
UNIVERSITY_EMAIL = ENV_TOKENS.get("UNIVERSITY_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
PRESS_EMAIL = ENV_TOKENS.get("PRESS_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
PAYMENT_SUPPORT_EMAIL = ENV_TOKENS.get("PAYMENT_SUPPORT_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
BULK_EMAIL_DEFAULT_FROM_EMAIL = ENV_TOKENS.get("BULK_EMAIL_DEFAULT_FROM_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
API_ACCESS_MANAGER_EMAIL = ENV_TOKENS.get("API_ACCESS_MANAGER_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
API_ACCESS_FROM_EMAIL = ENV_TOKENS.get("API_ACCESS_FROM_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])

# Get rid completely of coursewarehistoryextended, as we do not use the CSMH database
INSTALLED_APPS.remove("lms.djangoapps.coursewarehistoryextended")
DATABASE_ROUTERS.remove(
    "openedx.core.lib.django_courseware_routers.StudentModuleHistoryExtendedRouter"
)

# Set uploaded media file path
MEDIA_ROOT = "/openedx/media/"

# Video settings
VIDEO_IMAGE_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT
VIDEO_TRANSCRIPTS_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT

GRADES_DOWNLOAD = {
    "STORAGE_TYPE": "",
    "STORAGE_KWARGS": {
        "base_url": "/media/grades/",
        "location": "/openedx/media/grades",
    },
}

ORA2_FILEUPLOAD_BACKEND = "filesystem"
ORA2_FILEUPLOAD_ROOT = "/openedx/data/ora2"
ORA2_FILEUPLOAD_CACHE_NAME = "ora2-storage"

# Change syslog-based loggers which don't work inside docker containers
LOGGING["handlers"]["local"] = {
    "class": "logging.handlers.WatchedFileHandler",
    "filename": os.path.join(LOG_DIR, "all.log"),
    "formatter": "standard",
}
LOGGING["handlers"]["tracking"] = {
    "level": "DEBUG",
    "class": "logging.handlers.WatchedFileHandler",
    "filename": os.path.join(LOG_DIR, "tracking.log"),
    "formatter": "standard",
}
LOGGING["loggers"]["tracking"]["handlers"] = ["console", "local", "tracking"]
# Silence some loggers (note: we must attempt to get rid of these when upgrading from one release to the next)

import warnings
from django.utils.deprecation import RemovedInDjango40Warning, RemovedInDjango41Warning
warnings.filterwarnings("ignore", category=RemovedInDjango40Warning)
warnings.filterwarnings("ignore", category=RemovedInDjango41Warning)
warnings.filterwarnings("ignore", category=DeprecationWarning, module="lms.djangoapps.course_wiki.plugins.markdownedx.wiki_plugin")
warnings.filterwarnings("ignore", category=DeprecationWarning, module="wiki.plugins.links.wiki_plugin")

# Email
EMAIL_USE_SSL = False
# Forward all emails from edX's Automated Communication Engine (ACE) to django.
ACE_ENABLED_CHANNELS = ["django_email"]
ACE_CHANNEL_DEFAULT_EMAIL = "django_email"
ACE_CHANNEL_TRANSACTIONAL_EMAIL = "django_email"
EMAIL_FILE_PATH = "/tmp/openedx/emails"

# Language/locales
LOCALE_PATHS.append("/openedx/locale/contrib/locale")
LOCALE_PATHS.append("/openedx/locale/user/locale")
LANGUAGE_COOKIE_NAME = "openedx-language-preference"

# Allow the platform to include itself in an iframe
X_FRAME_OPTIONS = "SAMEORIGIN"


JWT_AUTH["JWT_ISSUER"] = "http://local.overhang.io/oauth2"
JWT_AUTH["JWT_AUDIENCE"] = "openedx"
JWT_AUTH["JWT_SECRET_KEY"] = "bNu0FXp77dOFFjn6eygBVKAt"
JWT_AUTH["JWT_PRIVATE_SIGNING_JWK"] = json.dumps(
    {
        "kid": "openedx",
        "kty": "RSA",
        "e": "AQAB",
        "d": "DGPnCN8XbZIPmPYwlH_2PSmKkuoRTVIztS6HlMRM4qRigqt1eJzV1YwVf_Od54Ba1PAAZDZ_3Tnb-M9U5OG__P-7ACF_-UWALTZdoDG9oBxnyJtel8L8_nJvdwJfEE6964IfDpAODA2YvZtC5mQk4aNqiX0le0Kdj1Z9lsYb05TLwBKxMmLmeMxhxtbQtJRumHLHUJS3J-S4Oy0J0EmyGMFNj_XP7w3f2FTrLdzRtG0DlB4eCWbe6T1n_9np_GQpxbUOZH3aAZGGJpXxzlVf1g7jORCiBG7Lk2BctUrTkKe29BCH1LDqAaCK3kFjNoUjqz3opr16WOnsg0UsxdiZUQ",
        "n": "xCPURKU-XxJgJ-7IBPr5o3rpxG4UvS_NAl1LpLkdXlDz0l0CelR-yXSv3PJDeFkwEH_1YKR85CgkxZWAIwnykOz0XcYg0hXbEPn97qWVwcuOiDvOuZriKQYN8Mc9QmZKV4_dag4i4c1YATyhXqxaY_HpjDlR5Ur-4lJsKsWKXofFCfeLirQuOyFYQy3ovXrflY510HBprkVmFOGcQs0AijD6U3WYOEq-dCbIwm6z-8j4TxiDdFE4S_LHdq-LdQAlYfQIyvsosgx0Zu70b5c8kyOcZUvGUnnnnf9noH9r7KizV4DOwfpwRVlwY3PPeXXRKtTBZiA0ZX7AhB_rXuEobQ",
        "p": "2tV5pimS-GabY-W__ERPewMLeBPda-Qz67kcj9lQ86UZRsRDWPb6rqkqcUbLPI8cHFUVPU4yUraZcnn2K-bERrdsTyrAZNVQndzg_7BWckH5UvV83wXsx38ahwVFGqsJ0pYV-jmvRkVor6jyEE4L7qxCPaihuJXBcWbLtrLSaYc",
        "q": "5XOpGj5-5nOivATYD-F6WKU5i4D2cITR5zIjOZgD8Qp6fswU0eA-Et84efBicSn4yxZaNJ4Go0njxHYNG-NvLu_b0MfKEc-nU3DR09VROmYFWoGgNmIFFhe5lk0YoDDYiHe9slLSSzvjHkxsYmvyxwQKPDfMFQQo0KYBV9r3y2s",
    }
)
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

# Enable/Disable some features globally
FEATURES["ENABLE_DISCUSSION_SERVICE"] = False
FEATURES["PREVENT_CONCURRENT_LOGINS"] = False
FEATURES["ENABLE_CORS_HEADERS"] = True

# CORS
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_INSECURE = True
CORS_ALLOW_HEADERS = corsheaders_default_headers + ('use-jwt-cookie',)

# Add your MFE and third-party app domains here
CORS_ORIGIN_WHITELIST = []

# Disable codejail support
# explicitely configuring python is necessary to prevent unsafe calls
import codejail.jail_code
codejail.jail_code.configure("python", "nonexistingpythonbinary", user=None)
# another configuration entry is required to override prod/dev settings
CODE_JAIL = {
    "python_bin": "nonexistingpythonbinary",
    "user": None,
}

FEATURES["ENABLE_DISCUSSION_SERVICE"] = True
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
VIDEO_IMAGE_SETTINGS["STORAGE_KWARGS"]["location"] = VIDEO_IMAGE_SETTINGS["STORAGE_KWARGS"]["location"].lstrip("/")
VIDEO_TRANSCRIPTS_SETTINGS["STORAGE_KWARGS"]["location"] = VIDEO_TRANSCRIPTS_SETTINGS["STORAGE_KWARGS"]["location"].lstrip("/")
GRADES_DOWNLOAD["STORAGE_KWARGS"]["location"] = GRADES_DOWNLOAD["STORAGE_KWARGS"]["location"].lstrip("/")
GRADES_DOWNLOAD["STORAGE_KWARGS"]["bucket"] = "openedx"

ORA2_FILEUPLOAD_BACKEND = "s3"
FILE_UPLOAD_STORAGE_BUCKET_NAME = "openedx"

AWS_S3_SIGNATURE_VERSION = "s3v4"



AWS_S3_USE_SSL = True
AWS_S3_SECURE_URLS = True
AWS_DEFAULT_ACL = None # inherit from the bucket
AWS_S3_ADDRESSING_STYLE = "auto"
AWS_AUTO_CREATE_BUCKET = False

AWS_S3_REGION_NAME = ""
AWS_QUERYSTRING_EXPIRE = 7 * 24 * 60 * 60  # 1 week: this is necessary to generate valid download urls

TIME_ZONE="Asia/Kolkata"
FEATURES["ENABLE_COURSE_DISCOVERY"]=False
FEATURES["ENABLE_DASHBOARD_SEARCH"]=False
######## End of settings common to LMS and CMS

######## Common CMS settings

STUDIO_NAME = u"My Open edX - Studio"

# Authentication
SOCIAL_AUTH_EDX_OAUTH2_SECRET = "006Tdc8jxw84FwFFZIIusv2l"
SOCIAL_AUTH_EDX_OAUTH2_URL_ROOT = "http://lms:8000"
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False  # scheme is correctly included in redirect_uri
SESSION_COOKIE_NAME = "studio_session_id"

MAX_ASSET_UPLOAD_FILE_SIZE_IN_MB = 100

FRONTEND_LOGIN_URL = LMS_ROOT_URL + '/login'
FRONTEND_REGISTER_URL = LMS_ROOT_URL + '/register'

# Create folders if necessary
for folder in [LOG_DIR, MEDIA_ROOT, STATIC_ROOT_BASE]:
    if not os.path.exists(folder):
        os.makedirs(folder)

COURSE_IMPORT_EXPORT_STORAGE = DEFAULT_FILE_STORAGE
USER_TASKS_ARTIFACT_STORAGE = DEFAULT_FILE_STORAGE

######## End of common CMS settings

# Setup correct webpack configuration file for development
WEBPACK_CONFIG_PATH = "webpack.dev.config.js"


