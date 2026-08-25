import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 1. Initialize the standard Django application layout
application = get_wsgi_application()

# 2. Wrap your application with WhiteNoise and explicitly point it to your media folder
application = WhiteNoise(application, root=settings.MEDIA_ROOT, prefix=settings.MEDIA_URL)
