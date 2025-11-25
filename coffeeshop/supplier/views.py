from django.views.generic import ListView
from .models import Supplier

class SupplierListView(ListView):
    model = Supplier
    # Django secara otomatis akan mencari template di:
    # <nama_app>/<nama_model>_list.html -> warga/warga_list.html
