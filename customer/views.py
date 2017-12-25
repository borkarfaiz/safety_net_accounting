from django.views.generic import ListView

from .models import Customer


# Create your views here.

class CustomerList(ListView):
    model = Customer
    context_object_name = 'customer_list'
