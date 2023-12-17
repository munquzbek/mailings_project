from django.urls import path

from mails.apps import MailsConfig
from mails.views import ClientCreateView, ClientListView, ClientDetailView, MessageCreateView, MessageListView, \
    MessageDetailView

app_name = MailsConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('view/<int:pk>/', ClientDetailView.as_view(), name='view'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('list_message/', MessageListView.as_view(), name='list_message'),
    path('view_message/<int:pk>/', MessageDetailView.as_view(), name='view_message')
]
