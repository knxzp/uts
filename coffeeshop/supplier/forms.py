from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        # Tentukan field mana saja dari model yang ingin ditampilkan di form
        fields = ['nama_perusahaan', 'nama_penanggung_jawab', 'jenis_biji', 'asal_biji', 'alamat', 'kontak',]
