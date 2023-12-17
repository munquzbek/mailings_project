from django.db import models


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




