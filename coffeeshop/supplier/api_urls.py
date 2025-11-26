from django.urls import path
from .views import SupplierListAPIView

urlpatterns = [
    path('supplier/', SupplierListAPIView.as_view(), name='api-supplier-list'),
]
