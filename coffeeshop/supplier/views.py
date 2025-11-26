from django.views.generic import ListView
from .models import Supplier
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Supplier, Customer, Barista, Order
from .forms import SupplierForm

class SupplierListView(ListView):
    model = Supplier

class SupplierDetailView(DetailView):
    model = Supplier
    
class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier/supplier_form.html'
    success_url = reverse_lazy('supplier-list')
