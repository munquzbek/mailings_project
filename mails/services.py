from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone


def send_mails(obj):
    now = timezone.now()
    current_time = now.time()
    print(f'Current Time: {current_time}')
    print(f'Send Time: {obj.send_time}')
    if current_time >= obj.send_time:
        print('we did it')
        # send_mail(
        #     subject='privet',
        #     message='You have a message:',
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[obj.client.email]
        # )
    else:
        print('not work')
