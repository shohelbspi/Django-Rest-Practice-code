"""
ASGI config for sh10_django_rest_crud_genericapi_mixin project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "sh10_django_rest_crud_genericapi_mixin.settings"
)

application = get_asgi_application()
