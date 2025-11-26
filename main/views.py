from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from inventory.models import Product, Category
from django.db.models import Sum, F


@login_required
def index(request):
    # Temel istatistikler
    total_products = Product.objects.filter(is_active=True).count()
    total_categories = Category.objects.count()
    low_stock_products = [p for p in Product.objects.filter(is_active=True) if p.is_low_stock]
    out_of_stock = Product.objects.filter(quantity=0, is_active=True).count()
    
    # Toplam stok değeri
    total_value = Product.objects.filter(is_active=True).aggregate(
        total=Sum(F('quantity') * F('unit_price'))
    )['total'] or 0
    
    # Son eklenen ürünler
    recent_products = Product.objects.select_related('category').order_by('-created_at')[:5]
    
    # Düşük stoklu ürünler (ilk 5)
    low_stock_list = Product.objects.filter(is_active=True).order_by('quantity')[:5]
    low_stock_list = [p for p in low_stock_list if p.is_low_stock]
    
    context = {
        'total_products': total_products,
        'total_categories': total_categories,
        'low_stock_count': len(low_stock_products),
        'out_of_stock': out_of_stock,
        'total_value': total_value,
        'recent_products': recent_products,
        'low_stock_list': low_stock_list,
    }
    
    return render(request, 'main/index.html', context)

