import os


# =============================================================================
# Which WEB_ENV?
# =============================================================================
# Valid options - local, dev, qa, prod
WEB_ENV = 'local'

# Branch and version number
BRANCH = 'dev'
VERSION = 'v0.0.0'
# =============================================================================
# PATHS
# =============================================================================
# Full filesystem path to the project.
# based on common.py is in <PROJECT_ROOT>/settings
PROJECT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            os.pardir)

DEBUG = True
# Name of the directory for the project.
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]

# Package/module name to import the root urlpatterns from for the project.
# ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME
ROOT_URLCONF = "settings.urls"

# Put strings here, like "/home/html/django_templates"
# or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    "crispy_forms",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': 'app_db',
        'USER': 'app_admin',
        'PASSWORD': "App_admin123",
        'HOST': '127.0.0.1',
        'PORT': '33060',
    }
}
CRISPY_TEMPLATE_PACK = 'bootstrap3'
ACCOUNTS_MIN_PASSWORD_LENGTH = "6"
SECRET_KEY = '57)p_wybgbiof@xaph3r=&t29d4yydl)-i(4px4kc&wwlah&k+'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# This fucking thing keeps on irritating but now it wont
STATIC_ROOT = PROJECT_ROOT + "static/"

STATIC_URL = "/static/"

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
# This fucking thing keeps on irritating but now it wont
