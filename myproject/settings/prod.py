from myproject.settings.base import *
DEBUG = False
ALLOWED_HOSTS = ['*']
if 'myapp' in INSTALLED_APPS:
    INSTALLED_APPS.remove('myapp')