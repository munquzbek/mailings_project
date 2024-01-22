from django.contrib import admin

from users.forms import UserBanForm
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone')

    def get_form(self, request, obj=None, change=False, **kwargs):
        if request.user.groups.filter(name='moders'):
            return UserBanForm
        return super(UserAdmin, self).get_form(request, obj=None, **kwargs)






