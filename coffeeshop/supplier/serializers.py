from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        # Tentukan field dari model Warga yang ingin kita ekspos di API
        fields = ['nama_perusahaan', 'nama_penanggung_jawab', 'jenis_biji', 'asal_biji', 'alamat', 'kontak',]
