from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .scheduler import scheduler
from mails.models import Message, Settings
from mails.services import send_mails


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
        obj = form.save()
        scheduler.add_job(send_mails, 'interval', minutes=1, args=[obj])
        return super().form_valid(form)


class SettingsListView(ListView):
    model = Settings

