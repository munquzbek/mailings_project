from django.db import models


class Client(models.Model):
    email = models.EmailField(max_length=254, verbose_name='Почта')
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    comment = models.TextField(verbose_name='Комметарий')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
