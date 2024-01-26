import logging
from datetime import datetime

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.mail import send_mail
from django.core.management.base import BaseCommand

from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from client.models import Client
from mails.models import Settings, Message, Logs

logger = logging.getLogger(__name__)

scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
scheduler.add_jobstore(DjangoJobStore(), "default")


def get_data():
    data = Settings.objects.all()
    models = []
    for d in data:
        if d.status in ['active', 'created']:
            d.client = Client.objects.get(pk=d.client_id)
            d.message = Message.objects.get(pk=d.message_id)
            d.save()
            models.append(d)
    return models


def send_every_day():
    current_time = datetime.now().time()
    obj = get_data()
    for o in obj:
        if o.period == 'day':
            if o.send_time <= current_time:
                o.status = 'finished'
                o.save()
                print(f'mail SENT: {o.message.title} '
                      f'send_time: {o.send_time} now: {current_time}')
                # send_mail(
                #         f'{obj.message.title}',
                #         obj.message.body,
                #         settings.EMAIL_HOST_USER,
                #         [obj.client.email],
                # )
                set_log_success(o)
            else:
                print(f'mail NOT SENT send time:{o.send_time} '
                      f'now: {current_time}')
                set_log_not_time(o)


def send_every_week():
    current_time = datetime.now().time()
    obj = get_data()
    for o in obj:
        if o.period == 'week':
            if o.send_time <= current_time:
                o.status = 'finished'
                o.save()
                print(f'mail SENT: {o.message.title} '
                      f'send_time: {o.send_time} now: {current_time}')
                # send_mail(
                #         f'{obj.message.title}',
                #         obj.message.body,
                #         settings.EMAIL_HOST_USER,
                #         [obj.client.email],
                # )
                set_log_success(o)
            else:
                print(f'mail NOT SENT send time:{o.send_time} '
                      f'now: {current_time}')
                set_log_not_time(o)


def send_every_month():
    current_time = datetime.now().time()
    obj = get_data()
    for o in obj:
        if o.period == 'month':
            if o.send_time <= current_time:
                o.status = 'finished'
                o.save()
                print(f'mail SENT: {o.message.title} '
                      f'send_time: {o.send_time} now: {current_time}')
                # send_mail(
                #         f'{obj.message.title}',
                #         obj.message.body,
                #         settings.EMAIL_HOST_USER,
                #         [obj.client.email],
                # )
                set_log_success(o)
            else:
                print(f'mail NOT SENT send time:{o.send_time} '
                      f'now: {current_time}')
                set_log_not_time(o)


def set_log_success(obj):
    current_time = datetime.now().date()
    log_instance = Logs(
        time_last_try=str(current_time),
        status_of_try='finished',
        server_response='Mail sent successfully.',
        settings=obj
    )
    log_instance.save()


def set_log_not_time(obj):
    current_time = datetime.now().date()
    log_instance = Logs(
        time_last_try=str(current_time),
        status_of_try='active',
        server_response='Mail not sent. Scheduled time not reached.',
        settings=obj
    )
    log_instance.save()


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler.add_job(
            send_every_day,
            trigger=CronTrigger(second="*/3"),
            id="send_every_day",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'send_every_day'.")

        scheduler.add_job(
            send_every_week,
            trigger=CronTrigger(day_of_week="fri", hour="*/1", minute="00"),
            id="send_every_week",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'send_every_week'.")

        scheduler.add_job(
            send_every_month,
            trigger=CronTrigger(month="*/1", day="1", hour="*/1", minute="00"),
            id="send_every_month",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'send_every_month'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
