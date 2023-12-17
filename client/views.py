from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from client.models import Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'name', 'surname', 'comment',)
    success_url = reverse_lazy('client:list')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client

