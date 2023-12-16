from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from mails.models import Client


def home(request):
    return render(request, 'mails/home.html')


class MailsCreateView(CreateView):
    model = Client
    fields = ('email', 'name', 'surname', 'comment',)
    success_url = reverse_lazy('home')
