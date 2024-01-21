
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config import settings
from users.forms import UserRegisterForm
from users.models import User


def success(request):
    context = {
        'title': 'Success sign up'
    }
    return render(request, 'users/success_signup.html', context)


def verified_email(request, token):
    try:
        user = get_object_or_404(User, token=token)
        if user:
            user.is_verified = True
            user.save()
            msg = 'Your email verified'
            return render(request, 'users/verified_email.html', {'msg': msg})
    except Exception as e:
        msg = e
        return render(request, 'users/verified_email.html', {'msg': msg})


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:success')

    def form_valid(self, form):
        self.object = form.save()
        domain_name = get_current_site(self.request).domain
        print(self.object)
        print(f'token user {self.object.token}')
        link = f'http://{domain_name}/users/verify/{str(self.object.token)}'
        print(link)

        send_mail(
            "Email Verification",
            f"Click the link-> {link} to verify",
            settings.EMAIL_HOST_USER,
            [self.object.email],
            fail_silently=False,
        )
        return super().form_valid(form)
