from django.contrib import admin

from mails.forms import SettingsOffForm
from mails.models import Message, Settings, Logs


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('send_time', 'period', 'status', 'message')

    def get_form(self, request, obj=None, change=False, **kwargs):
        if request.user.groups.filter(name='moders'):
            print('hellow')
            return SettingsOffForm
        return super(SettingsAdmin, self).get_form(request, obj=None, **kwargs)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('status_of_try', 'settings')

