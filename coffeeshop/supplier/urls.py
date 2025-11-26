from django.urls import path
from .views import SupplierListView, SupplierDetailView, SupplierCreateView, SupplierUpdateView, SupplierDeleteView

urlpatterns = [
    path('', SupplierListView.as_view(), name='supplier-list'),
    path('tambah/', SupplierCreateView.as_view(), name='supplier-tambah'), # URL untuk form tambah
    path('<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path('<int:pk>/edit/', SupplierUpdateView.as_view(), name='supplier-edit'),
    path('<int:pk>/edit/', SupplierUpdateView.as_view(), name='supplier-edit'),
    path('<int:pk>/hapus/', SupplierDeleteView.as_view(), name='supplier-hapus'), # URL untuk hapus

]
