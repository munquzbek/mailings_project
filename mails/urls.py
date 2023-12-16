from django.urls import path

from mails.apps import MailsConfig
from mails.views import ClientCreateView, ClientListView, ClientDetailView

app_name = MailsConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('view/<int:pk>/', ClientDetailView.as_view(), name='view'),
]
