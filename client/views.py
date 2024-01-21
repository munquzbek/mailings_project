from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from client.models import Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('email', 'name', 'surname', 'comment',)
    success_url = reverse_lazy('client:list')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

