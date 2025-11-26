from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Kategori Adı')
    description = models.TextField(blank=True, null=True, verbose_name='Açıklama')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ürün Adı')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name='Kategori')
    sku = models.CharField(max_length=50, unique=True, verbose_name='Stok Kodu', help_text='Benzersiz ürün kodu')
    description = models.TextField(blank=True, null=True, verbose_name='Açıklama')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Birim Fiyat')
    quantity = models.IntegerField(default=0, verbose_name='Miktar', help_text='Mevcut stok miktarı')
    min_stock_level = models.IntegerField(default=10, verbose_name='Minimum Stok Seviyesi', help_text='Bu seviyenin altında uyarı verilir')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Ürün Resmi')
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Oluşturan')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')

    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} ({self.sku})'

    @property
    def is_low_stock(self):
        return self.quantity <= self.min_stock_level

    @property
    def total_value(self):
        return self.quantity * self.unit_price


class StockMovement(models.Model):
    MOVEMENT_TYPES = (
        ('IN', 'Giriş'),
        ('OUT', 'Çıkış'),
        ('ADJUST', 'Düzeltme'),
    )
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='movements', verbose_name='Ürün')
    movement_type = models.CharField(max_length=10, choices=MOVEMENT_TYPES, verbose_name='İşlem Tipi')
    quantity = models.IntegerField(verbose_name='Miktar')
    note = models.TextField(blank=True, null=True, verbose_name='Not')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='İşlemi Yapan')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='İşlem Tarihi')
    
    class Meta:
        verbose_name = 'Stok Hareketi'
        verbose_name_plural = 'Stok Hareketleri'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.product.name} - {self.get_movement_type_display()} ({self.quantity})'
