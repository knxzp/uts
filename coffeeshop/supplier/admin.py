from django.contrib import admin
from .models import Supplier, Customer, Barista, Order

admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Barista)
admin.site.register(Order)