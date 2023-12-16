from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from mails.models import Client


# def home(request):
#     return render(request, 'mails/base.html')


class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'name', 'surname', 'comment',)
    success_url = reverse_lazy('mails:list')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


