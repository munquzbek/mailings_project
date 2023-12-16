from django.urls import path

from mails.views import home, MailsCreateView

urlpatterns = [
    path('', home, name='home'),
    path('create/', MailsCreateView.as_view(), name='create'),
]
