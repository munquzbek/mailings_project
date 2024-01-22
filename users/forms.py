from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserBanForm(ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)
