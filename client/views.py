from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from client.models import Client, Blog
from mails.models import Settings
from mails.views import UserIsVerified


def home(request):
    setups = Settings.objects.all()
    active_setups = Settings.objects.filter(status__in=['active', 'created'])
    clients = Client.objects.all()
    blogs = Blog.objects.all().order_by('-id')[:3]
    last_three = reversed(blogs)
    context = {
        'setups': setups,
        'active_setups': active_setups,
        'clients': clients,
        'blogs': last_three
    }
    return render(request, 'client/home.html', context)


class ClientCreateView(LoginRequiredMixin, UserIsVerified, CreateView):
    model = Client
    fields = ('email', 'name', 'surname', 'comment',)
    success_url = reverse_lazy('client:list')


class ClientListView(LoginRequiredMixin, UserIsVerified, ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, UserIsVerified, DetailView):
    model = Client

