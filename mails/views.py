from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

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
    fields = ('send_time', 'period', 'status', 'message', 'client')
    success_url = reverse_lazy('mails:list_setup')

    def form_valid(self, form):
        return super().form_valid(form)


class SettingsListView(ListView):
    model = Settings


class SettingsDetailView(DetailView):
    model = Settings


class SettingsUpdateView(UpdateView):
    model = Settings
    fields = ('send_time', 'period', 'status', 'message', 'client')
    success_url = reverse_lazy('mails:list_setup')
