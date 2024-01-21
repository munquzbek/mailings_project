import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Сообщение')),
                ('body', models.TextField(verbose_name='Тело сообщения')),
                ('create_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.TimeField(verbose_name='Время рассылки')),
                ('period', models.CharField(choices=[('day', 'day'), ('week', 'week'), ('month', 'month')], verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('created', 'created'), ('active', 'active'), ('finished', 'finished')], default='created')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='Клиент')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mails.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_last_try', models.DateTimeField(verbose_name='Дата и время последней попытки')),
                ('status_of_try', models.CharField(choices=[('failed', 'failed'), ('active', 'active'), ('finished', 'finished')], default='active', verbose_name='Статус попытки')),
                ('server_response', models.CharField(max_length=150, verbose_name='ответ сервера')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mails.settings', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]
