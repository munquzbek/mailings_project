from django.contrib import admin

from client.models import Client, Blog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    search_fields = ('name', 'comment')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_date', 'views_count')

