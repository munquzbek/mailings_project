from apscheduler.triggers.cron import CronTrigger
from django.utils import timezone
from smtplib import SMTPException
from django.core.mail import send_mail
from django.conf import settings
from mails.models import Logs, Settings

from apscheduler.schedulers.background import BackgroundScheduler

from datetime import datetime

# Create an instance of BackgroundScheduler
scheduler = BackgroundScheduler()


# setup times
now = timezone.now()
current_time = now.time()


def schedule_jobs():
    """
    Function to check period of mailing settings and schedule job for each options
    """
    # Get all mailing settings from the database
    mailings = Settings.objects.all()

    # Schedule jobs for each mailing due to provided period
    for mailing in mailings:
        print(f"Scheduling job for mailing {mailing.id}")
        if mailing.period == 'day':
            # Schedule a job to run 'send_mails' every day at the specified time
            scheduler.add_job(
                send_mails,
                trigger='cron',
                day_of_week='*',
                hour=mailing.send_time.hour,
                minute=mailing.send_time.minute,
                id=f'day_check_{mailing.id}',
                name='Run everyday',
            )

        elif mailing.period == 'week':
            # Schedule a job to run 'send_mails' every week at the specified time
            trigger = CronTrigger(day_of_week='Mon',
                                  hour=mailing.send_time.hour,
                                  minute=str(mailing.send_time.minute))
            scheduler.add_job(
                send_mails,
                trigger=trigger,
                id=f'week_check_{mailing.id}',
                name='Run every week',
            )

        else:
            # Schedule a job to run 'send_mails' on a specific day of the month at the specified time
            scheduler.add_job(
                send_mails,
                trigger='cron',
                day=1,
                hour=mailing.send_time.hour,
                minute=mailing.send_time.minute,
                id=f'month_check_{mailing.id}',
                name='Run every month',
            )
    scheduler.start()


def handle_email_sending(mailing):
    """
    Function to send email at specified time
    """
    try:
        print(f"current_time: {current_time}")
        print(f"mailing.send_time: {mailing.send_time}\n")

        # Check if the current time is past the scheduled time for sending emails
        if current_time >= mailing.send_time:
            print("Sending email...")
            # Uncomment and fill in the details for sending emails
            # send_mail(
            #     subject='privet',
            #     message='You have a message:',
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list=[obj.client.email]
            # )
            mailing.status = 'finished'
            mailing.save()

            # Log a successful email sending attempt
            log_instance = Logs(
                time_last_try=now,
                status_of_try='finished',
                server_response='Mail sent successfully.',
                settings=mailing
            )
            log_instance.save()
        else:
            # Log that the scheduled time for sending emails hasn't been reached yet
            print(f'{mailing.id} Email not sent. Scheduled time not reached. now {now}')
            mailing.status = 'active'
            mailing.save()
            log_instance = Logs(
                time_last_try=now,
                status_of_try='active',
                server_response='Mail not sent. Scheduled time not reached.',
                settings=mailing
            )
            log_instance.save()

    except SMTPException as e:
        # Log an error if there's an exception during email sending
        print(f'Error: {str(e)}')
        log_instance = Logs(
            time_last_try=now,
            status_of_try='failed',
            server_response=f'Error: {str(e)}',
            settings=mailing
        )
        log_instance.save()


def send_mails():
    # GEt all mailing settings from the database
    mailings = Settings.objects.all()

    # Iterate over each mailing setting
    for mailing in mailings:
        if mailing.status in ['active', 'created']:
            # If the mailing is active or created, attempt to send emails
            handle_email_sending(mailing)
        else:
            # If the mailing is neither active nor created, log that all jobs are finished
            print(f'{mailing.id} scheduled job finished')


def run():
    # Schedule jobs
    print('starts....')
    scheduler.add_job(send_mails, 'interval', minutes=1)
    scheduler.add_job(schedule_jobs, 'cron', hour=5, minute=35)

    # Start the scheduler after all jobs are added
    scheduler.start()



