from django.apps import AppConfig
from .scheduler import scheduler


class MailsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mails'



