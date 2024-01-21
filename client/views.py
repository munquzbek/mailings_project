from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from client.models import Client
from mails.views import UserIsVerified


class ClientCreateView(LoginRequiredMixin, UserIsVerified, CreateView):
    model = Client
    fields = ('email', 'name', 'surname', 'comment',)
    success_url = reverse_lazy('client:list')


class ClientListView(LoginRequiredMixin, UserIsVerified, ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, UserIsVerified, DetailView):
    model = Client

