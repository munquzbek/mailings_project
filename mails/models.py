from django.db import models


class Client(models.Model):
    email = models.EmailField(max_length=254, verbose_name='Почта')
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    comment = models.TextField(verbose_name='Комметарий')

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    title = models.CharField(max_length=200, verbose_name='Сообщение')
    body = models.TextField(verbose_name='Тело сообщения')
    create_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return {self.title}

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    class Admin:
        list_display = ('title', 'body')

# class Mailing(models.Model):
#     send_time = models.TimeField(auto_now=False, auto_now_add=False)

