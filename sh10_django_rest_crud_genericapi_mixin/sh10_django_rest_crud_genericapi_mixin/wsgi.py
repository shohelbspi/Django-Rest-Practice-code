"""
WSGI config for sh10_django_rest_crud_genericapi_mixin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "sh10_django_rest_crud_genericapi_mixin.settings"
)

application = get_wsgi_application()
