from django.contrib import admin

from mails.models import Message, Settings, Logs


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('send_time', 'period', 'status')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('status_of_try', 'settings')

