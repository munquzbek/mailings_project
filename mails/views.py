from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from mails.models import Message, Settings


class MessageCreateView(CreateView):
    model = Message
    fields = ('title', 'body',)
    success_url = reverse_lazy('mails:list_message')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class SettingsCreateView(CreateView):
    model = Settings
    fields = ('send_time', 'period', 'status')
    success_url = reverse_lazy('mails:list_setup')


class SettingsListView(ListView):
    model = Settings

