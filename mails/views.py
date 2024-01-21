from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mails.models import Message, Settings


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ('title', 'body',)
    success_url = reverse_lazy('mails:list_message')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class SettingsCreateView(LoginRequiredMixin, CreateView):
    model = Settings
    fields = ('send_time', 'period', 'status', 'message', 'client')
    success_url = reverse_lazy('mails:list_setup')


class SettingsListView(LoginRequiredMixin, ListView):
    model = Settings

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     for data in context_data['object_list']:
    #         status_check_and_send(data)
    #     return context_data


class SettingsDetailView(LoginRequiredMixin, DetailView):
    model = Settings


class SettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Settings
    fields = ('send_time', 'period', 'status', 'message', 'client')
    success_url = reverse_lazy('mails:list_setup')


class SettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = Settings
    success_url = reverse_lazy('mails:list_setup')
