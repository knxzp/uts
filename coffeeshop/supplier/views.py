from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Supplier, Customer, Barista, Order
from .forms import SupplierForm
from rest_framework.generics import ListAPIView
from .serializers import SupplierSerializer 
from rest_framework import viewsets

class SupplierListView(ListView):
    model = Supplier

class SupplierDetailView(DetailView):
    model = Supplier

class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier/supplier_form.html'
    success_url = reverse_lazy('supplier-list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier/supplier_form.html'  
    success_url = reverse_lazy('supplier-list')

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'supplier/supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier-list')

class SupplierListAPIView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
