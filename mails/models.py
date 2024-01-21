from django.db import models

from client.models import Client
from users.models import User, NULLABLE

# Period choices for Settings
PERIOD_CHOICES = (
    ("day", "day"),
    ("week", "week"),
    ("month", "month"),
)

# Status choices for Settings
STATUS_CHOICES = (
    ("created", "created"),
    ("active", "active"),
    ("finished", "finished")
)

# Statuses for Logs
STATUS_OF_TRY = (
    ("failed", "failed"),
    ("active", "active"),
    ("finished", "finished")
)


# Models
class Message(models.Model):
    title = models.CharField(max_length=200, verbose_name='Сообщение')
    body = models.TextField(verbose_name='Тело сообщения')
    create_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Settings(models.Model):
    # auto_now=False, auto_now_add=False to create by yourself
    send_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Время рассылки')
    period = models.CharField(choices=PERIOD_CHOICES, verbose_name='Периодичность')
    status = models.CharField(choices=STATUS_CHOICES, default="created")

    # on_delete=models.CASCADE if you delete message or client it deletes Settings also
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, **NULLABLE, verbose_name='Автор')

    def __str__(self):
        return f'id:{self.pk}, {self.send_time} per ({self.period}), {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Logs(models.Model):
    time_last_try = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Дата и время последней попытки')
    status_of_try = models.CharField(choices=STATUS_OF_TRY, default='active', verbose_name='Статус попытки')
    server_response = models.CharField(max_length=150, verbose_name='ответ сервера')

    settings = models.ForeignKey(Settings, on_delete=models.CASCADE, verbose_name='Рассылка')

    def __str__(self):
        return f'{self.status_of_try}, {self.time_last_try}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
