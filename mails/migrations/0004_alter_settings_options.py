# Generated by Django 4.2.7 on 2024-01-22 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0003_alter_settings_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'permissions': [('can_change_status', 'Can change status of settings')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]
