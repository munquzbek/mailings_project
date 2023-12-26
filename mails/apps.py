from django.apps import AppConfig


class MailsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mails'

    def ready(self):
        from mails.services import run
        run()
        print('started')

