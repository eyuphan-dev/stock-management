from django.contrib import admin
from .models import Category, Product, StockMovement


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'category', 'quantity', 'unit_price', 'stock_status', 'is_active']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'sku']
    list_editable = ['quantity', 'is_active']
    list_per_page = 20
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('name', 'sku', 'category', 'description')
        }),
        ('Fiyat ve Stok', {
            'fields': ('unit_price', 'quantity', 'min_stock_level')
        }),
        ('Diğer Bilgiler', {
            'fields': ('image', 'is_active', 'created_by', 'created_at', 'updated_at')
        }),
    )
    
    def stock_status(self, obj):
        if obj.is_low_stock:
            return '⚠️ Düşük Stok'
        return '✓ Normal'
    stock_status.short_description = 'Stok Durumu'


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ['product', 'movement_type', 'quantity', 'created_by', 'created_at']
    list_filter = ['movement_type', 'created_at']
    search_fields = ['product__name', 'product__sku', 'note']
    readonly_fields = ['created_at']
    list_per_page = 50
    
    fieldsets = (
        ('Hareket Bilgileri', {
            'fields': ('product', 'movement_type', 'quantity', 'note')
        }),
        ('Kayıt Bilgileri', {
            'fields': ('created_by', 'created_at')
        }),
    )
