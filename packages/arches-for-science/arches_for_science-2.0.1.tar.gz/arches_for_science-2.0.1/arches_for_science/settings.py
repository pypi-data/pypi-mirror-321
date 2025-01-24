"""
Django settings for arches_for_science project.
"""

import os
import arches
import inspect
import semantic_version
from datetime import datetime, timedelta
from django.utils.translation import gettext_lazy as _

try:
    from arches.settings import *
except ImportError:
    pass

APP_NAME = "arches_for_science"
APP_VERSION = semantic_version.Version(major=0, minor=0, patch=0)
APP_ROOT = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

WEBPACK_LOADER = {
    "DEFAULT": {
        "STATS_FILE": os.path.join(APP_ROOT, "..", "webpack/webpack-stats.json"),
    },
}

DATATYPE_LOCATIONS.append("arches_for_science.datatypes")
FUNCTION_LOCATIONS.append("arches_for_science.functions")
ETL_MODULE_LOCATIONS.append("arches_for_science.etl_modules")
SEARCH_COMPONENT_LOCATIONS.append("arches_for_science.search_components")

LOCALE_PATHS.insert(0, os.path.join(APP_ROOT, "locale"))

FILE_TYPE_CHECKING = "lenient"
FILE_TYPES = [
    "bmp",
    "gif",
    "jpg",
    "jpeg",
    "json",
    "pdf",
    "png",
    "psd",
    "rtf",
    "tif",
    "tiff",
    "xlsx",
    "csv",
    "zip",
]
FILENAME_GENERATOR = "arches.app.utils.storage_filename_generator.generate_filename"
UPLOADED_FILES_DIR = "uploadedfiles"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "#f56+u&mpoz^s&2qjk!v1j(jc&zr1*ana9z5q=7!246cx-1(iv"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ROOT_URLCONF = "arches_for_science.urls"
ELASTICSEARCH_HOSTS = [{"scheme": "http", "host": "localhost", "port": 9200}]
ELASTICSEARCH_CONNECTION_OPTIONS = {"request_timeout": 30, "verify_certs": False}
# ELASTICSEARCH_CONNECTION_OPTIONS = {"request_timeout": 30, "verify_certs": False, "basic_auth": ("elastic", "E1asticSearchforArche5")}
ELASTICSEARCH_PREFIX = "arches_for_science"

LOAD_DEFAULT_ONTOLOGY = False
LOAD_PACKAGE_ONTOLOGIES = True

# This is the namespace to use for export of data (for RDF/XML for example)
# It must point to the url where you host your site
# Make sure to use a trailing slash
ARCHES_NAMESPACE_FOR_DATA_EXPORT = "http://localhost:8000/"
PUBLIC_SERVER_ADDRESS = "http://localhost:8002/"

DATABASES = {
    "default": {
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "CONN_MAX_AGE": 0,
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": "localhost",
        "NAME": "arches_for_science",
        "OPTIONS": {
            "options": "-c cursor_tuple_fraction=1",
        },
        "PASSWORD": "postgis",
        "PORT": "5432",
        "POSTGIS_TEMPLATE": "template_postgis",
        "TEST": {"CHARSET": None, "COLLATION": None, "MIRROR": None, "NAME": None},
        "TIME_ZONE": None,
        "USER": "postgres",
    }
}

SEARCH_THUMBNAILS = False

INSTALLED_APPS = (
    "webpack_loader",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "arches",
    "arches.app.models",
    "arches.management",
    "guardian",
    "captcha",
    "revproxy",
    "corsheaders",
    "oauth2_provider",
    "django_celery_results",
    "pgtrigger",
    "arches_templating",
    # "silk",
    "arches_for_science",  # Ensure the project is listed before any other arches applications
)

# Placing this last ensures any templates provided by Arches Applications
# take precedence over core arches templates in arches/app/templates.
INSTALLED_APPS += ("arches.app",)

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    #'arches.app.utils.middleware.TokenMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "arches.app.utils.middleware.ModifyAuthorizationHeader",
    "oauth2_provider.middleware.OAuth2TokenMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "arches.app.utils.middleware.SetAnonymousUser",
    # "silk.middleware.SilkyMiddleware",
]

STATICFILES_DIRS = build_staticfiles_dirs(app_root=APP_ROOT)

TEMPLATES = build_templates_config(
    debug=DEBUG,
    app_root=APP_ROOT,
)

ALLOWED_HOSTS = []

SYSTEM_SETTINGS_LOCAL_PATH = os.path.join(APP_ROOT, "system_settings", "System_Settings.json")
WSGI_APPLICATION = "arches_for_science.wsgi.application"

# URL that handles the media served from MEDIA_ROOT, used for managing stored files.
# It must end in a slash if set to a non-empty value.
MEDIA_URL = "/files/"

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(APP_ROOT)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(APP_ROOT, "staticfiles")

# when hosting Arches under a sub path set this value to the sub path eg : "/{sub_path}/"
FORCE_SCRIPT_NAME = None

RESOURCE_IMPORT_LOG = os.path.join(APP_ROOT, "logs", "resource_import.log")
DEFAULT_RESOURCE_IMPORT_USER = {"username": "admin", "userid": 1}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        },
    },
    "handlers": {
        "file": {
            "level": "WARNING",  # DEBUG, INFO, WARNING, ERROR
            "class": "logging.FileHandler",
            "filename": os.path.join(APP_ROOT, "arches.log"),
            "formatter": "console",
        },
        "console": {"level": "WARNING", "class": "logging.StreamHandler", "formatter": "console"},
    },
    "loggers": {"arches": {"handlers": ["file", "console"], "level": "WARNING", "propagate": True}},
}

# Rate limit for authentication views
# See options (including None or python callables):
# https://django-ratelimit.readthedocs.io/en/stable/rates.html#rates-chapter
RATE_LIMIT = "5/m"

# Sets default max upload size to 15MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640

# Unique session cookie ensures that logins are treated separately for each app
SESSION_COOKIE_NAME = "arches_for_science"

# For more info on configuring your cache: https://docs.djangoproject.com/en/2.2/topics/cache/
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    },
    "user_permission": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "user_permission_cache",
    },
}

# Hide nodes and cards in a report that have no data
HIDE_EMPTY_NODES_IN_REPORT = False

BYPASS_UNIQUE_CONSTRAINT_TILE_VALIDATION = False
BYPASS_REQUIRED_VALUE_TILE_VALIDATION = False

DATE_IMPORT_EXPORT_FORMAT = "%Y-%m-%d"  # Custom date format for dates imported from and exported to csv

# This is used to indicate whether the data in the CSV and SHP exports should be
# ordered as seen in the resource cards or not.
EXPORT_DATA_FIELDS_IN_CARD_ORDER = False

# Identify the usernames and duration (seconds) for which you want to cache the time wheel
CACHE_BY_USER = {"default": 3600 * 24, "anonymous": 3600 * 24}  # 24hrs  # 24hrs

TILE_CACHE_TIMEOUT = 600  # seconds
CLUSTER_DISTANCE_MAX = 5000  # meters
GRAPH_MODEL_CACHE_TIMEOUT = None

OAUTH_CLIENT_ID = ""  #'9JCibwrWQ4hwuGn5fu2u1oRZSs9V6gK8Vu8hpRC4'

APP_TITLE = "Arches | Heritage Data Management"
COPYRIGHT_TEXT = "All Rights Reserved."
COPYRIGHT_YEAR = "2019"

ENABLE_CAPTCHA = False
# RECAPTCHA_PUBLIC_KEY = ''
# RECAPTCHA_PRIVATE_KEY = ''
# RECAPTCHA_USE_SSL = False
NOCAPTCHA = True
# RECAPTCHA_PROXY = 'http://127.0.0.1:8000'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  #<-- Only need to uncomment this for testing without an actual email server
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "xxxx@xxx.com"
# EMAIL_HOST_PASSWORD = 'xxxxxxx'
# EMAIL_PORT = 587

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

CELERY_BROKER_URL = ""  # RabbitMQ --> "amqp://guest:guest@localhost",  Redis --> "redis://localhost:6379/0"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_RESULT_BACKEND = "django-db"  # Use 'django-cache' if you want to use your cache as your backend
CELERY_TASK_SERIALIZER = "json"


CELERY_SEARCH_EXPORT_EXPIRES = 24 * 3600  # seconds
CELERY_SEARCH_EXPORT_CHECK = 3600  # seconds

CELERY_BEAT_SCHEDULE = {
    "delete-expired-search-export": {
        "task": "arches.app.tasks.delete_file",
        "schedule": CELERY_SEARCH_EXPORT_CHECK,
    },
    "notification": {
        "task": "arches.app.tasks.message",
        "schedule": CELERY_SEARCH_EXPORT_CHECK,
        "args": ("Celery Beat is Running",),
    },
}

# Set to True if you want to send celery tasks to the broker without being able to detect celery.
# This might be necessary if the worker pool is regulary fully active, with no idle workers, or if
# you need to run the celery task using solo pool (e.g. on Windows). You may need to provide another
# way of monitoring celery so you can detect the background task not being available.
CELERY_CHECK_ONLY_INSPECT_BROKER = False

CANTALOUPE_DIR = os.path.join(ROOT_DIR, UPLOADED_FILES_DIR)
CANTALOUPE_HTTP_ENDPOINT = "http://localhost:8182/"

ACCESSIBILITY_MODE = False

RENDERERS = [
    {
        "name": "imagereader",
        "title": "Image Reader",
        "description": "Displays most image file types",
        "id": "5e05aa2e-5db0-4922-8938-b4d2b7919733",
        "iconclass": "fa fa-camera",
        "component": "views/components/cards/file-renderers/imagereader",
        "ext": "",
        "type": "image/*",
        "exclude": "tif,tiff,psd",
    },
    {
        "name": "pdfreader",
        "title": "PDF Reader",
        "description": "Displays pdf files",
        "id": "09dec059-1ee8-4fbd-85dd-c0ab0428aa94",
        "iconclass": "fa fa-file",
        "component": "views/components/cards/file-renderers/pdfreader",
        "ext": "pdf",
        "type": "application/pdf",
        "exclude": "tif,tiff,psd",
    },
]

# By setting RESTRICT_MEDIA_ACCESS to True, media file requests outside of Arches will checked against nodegroup permissions.
RESTRICT_MEDIA_ACCESS = False

# By setting RESTRICT_CELERY_EXPORT_FOR_ANONYMOUS_USER to True, if the user is attempting
# to export search results above the SEARCH_EXPORT_IMMEDIATE_DOWNLOAD_THRESHOLD
# value and is not signed in with a user account then the request will not be allowed.
RESTRICT_CELERY_EXPORT_FOR_ANONYMOUS_USER = False

# Dictionary containing any additional context items for customising email templates
EXTRA_EMAIL_CONTEXT = {
    "salutation": _("Hi"),
    "expiration": (datetime.now() + timedelta(seconds=CELERY_SEARCH_EXPORT_EXPIRES)).strftime("%A, %d %B %Y"),
}

# see https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#how-django-discovers-language-preference
# to see how LocaleMiddleware tries to determine the user's language preference
# (make sure to check your accept headers as they will override the LANGUAGE_CODE setting!)
# also see get_language_from_request in django.utils.translation.trans_real.py
# to see how the language code is derived in the actual code

####### TO GENERATE .PO FILES DO THE FOLLOWING ########
# run the following commands
# language codes used in the command should be in the form (which is slightly different
# form the form used in the LANGUAGE_CODE and LANGUAGES settings below):
# --local={countrycode}_{REGIONCODE} <-- countrycode is lowercase, regioncode is uppercase, also notice the underscore instead of hyphen
# commands to run (to generate files for "British English, German, and Spanish"):
# django-admin.py makemessages --ignore=env/* --local=de --local=en --local=en_GB --local=es  --extension=htm,py
# django-admin.py compilemessages


# default language of the application
# language code needs to be all lower case with the form:
# {langcode}-{regioncode} eg: en, en-gb ....
# a list of language codes can be found here http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en"

# list of languages to display in the language switcher,
# if left empty or with a single entry then the switch won't be displayed
# language codes need to be all lower case with the form:
# {langcode}-{regioncode} eg: en, en-gb ....
# a list of language codes can be found here http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGES = [
    #   ('de', _('German')),
    ("en", _("English")),
    #   ('en-gb', _('British English')),
    #   ('es', _('Spanish')),
]

# override this to permenantly display/hide the language switcher
SHOW_LANGUAGE_SWITCH = len(LANGUAGES) > 1

# try:
#     from .package_settings import *
# except ImportError:
#     try:
#         from package_settings import *
#     except ImportError as e:
#         pass

# try:
#     from .settings_local import *
# except ImportError as e:
#     try:
#         from settings_local import *
#     except ImportError as e:
#         pass
