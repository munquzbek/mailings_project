from django.contrib import admin
from django.forms import ModelForm

from users.models import User


class UserBanForm(ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        if request.user.groups.filter(name='moders'):
            print('hellow')
            return UserBanForm
        return super(UserAdmin, self).get_form(request, obj=None, **kwargs)






