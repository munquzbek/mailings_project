from django.urls import path

from mails.views import home

urlpatterns = [
    path('', home)
]
