from django.urls import path

from client.apps import ClientConfig

from client.views import ClientListView, ClientCreateView, ClientDetailView, home

app_name = ClientConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('client_list', ClientListView.as_view(), name='list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('view/<int:pk>/', ClientDetailView.as_view(), name='view'),
]
