"""
ARCHES - a program developed to inventory and manage immovable cultural heritage.
Copyright (C) 2013 J. Paul Getty Trust and World Monuments Fund

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from arches.settings import *
from arches_for_science.settings import *
import arches
import os

try:
    from django.utils.translation import gettext_lazy as _
except ImportError:  # unable to import prior to installing requirements
    pass

APP_ROOT = os.path.dirname(__file__)
TEST_ROOT = os.path.normpath(os.path.join(ROOT_DIR, "..", "tests"))


MIN_ARCHES_VERSION = arches.__version__
MAX_ARCHES_VERSION = arches.__version__

# LOAD_V3_DATA_DURING_TESTS = True will engage the most extensive the of the v3
# data migration tests, which could add over a minute to the test process. It's
# recommended that this setting only be set to True in tests/settings_local.py
# and run in specific cases at the discretion of the developer.
LOAD_V3_DATA_DURING_TESTS = False

RESOURCE_GRAPH_LOCATIONS = (os.path.join(TEST_ROOT, "fixtures", "resource_graphs"),)

ONTOLOGY_FIXTURES = os.path.join(TEST_ROOT, "fixtures", "ontologies", "test_ontology")
ONTOLOGY_PATH = os.path.join(TEST_ROOT, "fixtures", "ontologies", "cidoc_crm")
MEDIA_ROOT = os.path.join(TEST_ROOT, "fixtures", "data")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "arches",
    "arches.app.models",
    "arches.management",
    "guardian",
    "oauth2_provider",
    "pgtrigger",
    "arches_templating",
    "arches_for_science",
]

DATABASES = {
    "default": {
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "CONN_MAX_AGE": 0,
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": "localhost",
        "NAME": "arches_for_science",
        "OPTIONS": {},
        "PASSWORD": "postgis",
        "PORT": "5432",
        "POSTGIS_TEMPLATE": "template_postgis",
        "TEST": {"CHARSET": None, "COLLATION": None, "MIRROR": None, "NAME": None},
        "TIME_ZONE": None,
        "USER": "postgres",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    },
    "user_permission": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        "LOCATION": "user_permission_cache",
    },
}

LOGGING["loggers"]["arches"]["level"] = "ERROR"

ELASTICSEARCH_PREFIX = "test"

TEST_RUNNER = "arches.test.runner.ArchesTestRunner"
SILENCED_SYSTEM_CHECKS.append("arches.W001")  # Cache backend does not support rate-limiting

# could add Chrome, PhantomJS etc... here
LOCAL_BROWSERS = []  # ['Firefox']

ENABLE_USER_SIGNUP = True
FORCE_USER_SIGNUP_EMAIL_AUTHENTICATION = True

OVERRIDE_RESOURCE_MODEL_LOCK = True

ENABLE_TWO_FACTOR_AUTHENTICATION = False
FORCE_TWO_FACTOR_AUTHENTICATION = False

DATATYPE_LOCATIONS.append("tests.fixtures.datatypes")
ELASTICSEARCH_HOSTS = [{"scheme": "http", "host": "localhost", "port": ELASTICSEARCH_HTTP_PORT}]
LANGUAGES = [
    ("de", _("German")),
    ("en", _("English")),
    ("en-gb", _("British English")),
    ("es", _("Spanish")),
    ("ar", _("Arabic")),
]

DOCKER = False
