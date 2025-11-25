from django.db import models

class Supplier(models.Model):
    nama_perusahaan = models.CharField(max_length=100, verbose_name="Nama Perusahaan")
    nama_penanggung_jawab = models.CharField(max_length=100, verbose_name="Nama Penanggung Jawab")
    jenis_biji = models.CharField(max_length=100, verbose_name="Jenis Biji Kopi")  # Arabica, Robusta, Blend
    asal_biji = models.CharField(max_length=100, verbose_name="Asal Biji Kopi")   # Gayo, Toraja, Bali Kintamani
    alamat = models.TextField(verbose_name="Alamat Supplier")
    kontak = models.CharField(max_length=20, verbose_name="Nomor Kontak")
    tanggal_kerjasama = models.DateField(auto_now_add=True, verbose_name="Tanggal Mulai Kerjasama")

    def __str__(self):
        return self.nama_perusahaan
    
class Customer(models.Model):
    nama_lengkap = models.CharField(max_length=100, verbose_name="Nama Lengkap")
    email = models.EmailField(max_length=100, verbose_name="Email")
    no_telepon = models.CharField(max_length=20, verbose_name="Nomor Telepon")
    alamat = models.TextField(verbose_name="Alamat Tinggal")
    tanggal_daftar = models.DateField(auto_now_add=True, verbose_name="Tanggal Daftar")

    def __str__(self):
        return self.nama_lengkap
    
class Barista(models.Model):
    STATUS_CHOICES = [
        ('PAGI', 'Pagi'),
        ('SIANG', 'Siang'),
        ('MALAM', 'Malam'),
    ]
    nama_lengkap = models.CharField(max_length=100, verbose_name="Nama Barista")
    no_telepon = models.CharField(max_length=20, verbose_name="Nomor Telepon")
    shift = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PAGI')  # Pagi / Siang / Malam
    tanggal_mulai = models.DateField(auto_now_add=True, verbose_name="Tanggal Mulai Bekerja")

    def __str__(self):
        return self.nama_lengkap
       
class Order(models.Model):
    STATUS_CHOICES = [
        ('MENUNGGU', 'Menunggu'),
        ('DIPROSES', 'Diproses'),
        ('SELESAI', 'Selesai'),
    ]
    nama_menu = models.CharField(max_length=200)
    catatan = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='MENUNGGU')
    tanggal_pesan = models.DateTimeField(auto_now_add=True)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    barista = models.ForeignKey(Barista, on_delete=models.SET_NULL, null=True, related_name='orders')
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, related_name='orders')
   
    def __str__(self):
        return self.nama_menu