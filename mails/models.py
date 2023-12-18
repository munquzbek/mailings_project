from django.db import models

PERIOD_CHOICES = (
    ("day", "day"),
    ("week", "week"),
    ("month", "month"),
)

STATUS_CHOICES = (
    ("created", "created"),
    ("active", "active"),
    ("finished", "finished")
)


class Message(models.Model):
    title = models.CharField(max_length=200, verbose_name='Сообщение')
    body = models.TextField(verbose_name='Тело сообщения')
    create_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    class Admin:
        list_display = ('title', 'body')


class Settings(models.Model):
    send_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Время рассылки')
    period = models.CharField(choices=PERIOD_CHOICES, verbose_name='Периодичность')
    status = models.CharField(choices=STATUS_CHOICES, default="created")

    def __str__(self):
        return f'at {self.send_time} per ({self.period}), {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


