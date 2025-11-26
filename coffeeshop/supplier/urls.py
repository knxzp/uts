from django.urls import path
from .views import SupplierListView, SupplierDetailView, SupplierCreateView

urlpatterns = [
    path('', SupplierListView.as_view(), name='supplier-list'),
    path('tambah/', SupplierCreateView.as_view(), name='supplier-tambah'), # URL untuk form tambah
    path('<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),

]
