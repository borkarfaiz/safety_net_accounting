from django.urls import path

from .views import CustomerList

app_name = 'polls'

urlpatterns = [
    path('', CustomerList.as_view(), name='list'),
]
