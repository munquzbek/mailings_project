from django.urls import path

from mails.apps import MailsConfig
from mails.views import MessageCreateView, MessageListView, MessageDetailView, SettingsCreateView, SettingsListView, \
    SettingsDetailView, SettingsUpdateView, SettingsDeleteView

app_name = MailsConfig.name

urlpatterns = [
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('list_message/', MessageListView.as_view(), name='list_message'),
    path('view_message/<int:pk>/', MessageDetailView.as_view(), name='view_message'),
    path('setup/', SettingsCreateView.as_view(), name='create_setup'),
    path('list_setup/', SettingsListView.as_view(), name='list_setup'),
    path('view_setup/<int:pk>/', SettingsDetailView.as_view(), name='view_setup'),
    path('update_setup/<int:pk>/', SettingsUpdateView.as_view(), name='update_setup'),
    path('delete_setup/<int:pk>/', SettingsDeleteView.as_view(), name='delete_setup'),
]
