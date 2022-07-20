"""
WSGI config for razorpay_bot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application
# from dj_static import Cling

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'razorpay_bot.settings')

# application = Cling(get_wsgi_application())

import os
from django.conf import settings
from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_obs.settings')