from myproject.settings.base import *
DEBUG = True
if 'myapp' not in INSTALLED_APPS:
    INSTALLED_APPS.append('myapp')