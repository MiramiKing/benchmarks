from django.core.wsgi import get_wsgi_application
from django.conf import settings

from . import views


settings.configure(
    SECRET_KEY='nosecret',
    DEBUG=False,
    ROOT_URLCONF=views,
    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

)

app = get_wsgi_application()
