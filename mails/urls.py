from django.urls import path

from mails.apps import MailsConfig
from mails.views import MessageCreateView, MessageListView, MessageDetailView, SettingsCreateView, SettingsListView

app_name = MailsConfig.name

urlpatterns = [
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('list_message/', MessageListView.as_view(), name='list_message'),
    path('view_message/<int:pk>/', MessageDetailView.as_view(), name='view_message'),
    path('setup/', SettingsCreateView.as_view(), name='create_setup'),
    path('list_setup/', SettingsListView.as_view(), name='list_setup'),
]
