from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse, Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mails.forms import SettingsCreateForm
from mails.models import Message, Settings


class UserIsVerified(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_verified

    def handle_no_permission(self):
        return redirect('users:need_verify')


class MessageCreateView(LoginRequiredMixin, UserIsVerified, CreateView):
    model = Message
    fields = ('title', 'body',)
    success_url = reverse_lazy('mails:list_message')


class MessageListView(LoginRequiredMixin, UserIsVerified, ListView):
    model = Message


class MessageDetailView(LoginRequiredMixin, UserIsVerified, DetailView):
    model = Message


class SettingsCreateView(LoginRequiredMixin, UserIsVerified, CreateView):
    model = Settings
    form_class = SettingsCreateForm
    success_url = reverse_lazy('mails:list_setup')

    def form_valid(self, form):
        self.object = form.save()
        author = self.request.user
        self.object.author = author
        return super().form_valid(form)


class SettingsListView(LoginRequiredMixin, UserIsVerified, ListView):
    model = Settings

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     for data in context_data['object_list']:
    #         status_check_and_send(data)
    #     return context_data


class SettingsDetailView(LoginRequiredMixin, UserIsVerified, DetailView):
    model = Settings


class SettingsUpdateView(LoginRequiredMixin, UserIsVerified, UpdateView):
    model = Settings
    fields = ('send_time', 'period', 'status', 'message', 'client')
    success_url = reverse_lazy('mails:list_setup')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.author != self.request.user:
            raise Http404
        return self.object


class SettingsDeleteView(LoginRequiredMixin, UserIsVerified, DeleteView):
    model = Settings
    success_url = reverse_lazy('mails:list_setup')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.author != self.request.user:
            raise Http404
        return self.object

