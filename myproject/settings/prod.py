from myproject.settings.base import *
from myproject.urls import urlpatterns
#if 'myapp' in INSTALLED_APPS:
#    INSTALLED_APPS.remove('myapp')
urlpatterns.remove('accounts/')
DEBUG = False
ALLOWED_HOSTS = ['*']