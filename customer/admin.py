from django.contrib import admin

from .models import Customer


# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'created',)


admin.site.register(Customer, AdminCustomer)
