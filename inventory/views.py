from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Category, StockMovement
from .forms import ProductForm, CategoryForm


@login_required
def product_list(request):
    products = Product.objects.select_related('category').all()
    
    # Arama
    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search) | products.filter(sku__icontains=search)
    
    # Kategori filtresi
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    
    # Stok durumu filtresi
    stock_filter = request.GET.get('stock')
    if stock_filter == 'low':
        products = [p for p in products if p.is_low_stock]
    elif stock_filter == 'out':
        products = products.filter(quantity=0)
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'search': search,
        'selected_category': category_id,
        'stock_filter': stock_filter,
    }
    return render(request, 'inventory/product_list.html', context)


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    movements = product.movements.all()[:10]  # Son 10 hareket
    context = {
        'product': product,
        'movements': movements,
    }
    return render(request, 'inventory/product_detail.html', context)


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            messages.success(request, f'{product.name} başarıyla eklendi!')
            return redirect('inventory:product_list')
    else:
        form = ProductForm()
    
    context = {'form': form, 'title': 'Yeni Ürün Ekle'}
    return render(request, 'inventory/product_form.html', context)


@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} güncellendi!')
            return redirect('inventory:product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    
    context = {'form': form, 'product': product, 'title': 'Ürün Düzenle'}
    return render(request, 'inventory/product_form.html', context)


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'{product_name} silindi!')
        return redirect('inventory:product_list')
    
    context = {'product': product}
    return render(request, 'inventory/product_confirm_delete.html', context)


@login_required
def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'inventory/category_list.html', context)


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'{category.name} kategorisi başarıyla eklendi!')
            return redirect('inventory:category_list')
    else:
        form = CategoryForm()
    
    context = {'form': form, 'title': 'Yeni Kategori Ekle'}
    return render(request, 'inventory/category_form.html', context)


@login_required
def reports(request):
    from django.db.models import Sum, Count, F, Q
    from datetime import datetime, timedelta
    
    # Tarih filtresi
    date_filter = request.GET.get('date_filter', '30')  # Default 30 gün
    if date_filter == '7':
        start_date = datetime.now() - timedelta(days=7)
        period_name = 'Son 7 Gün'
    elif date_filter == '30':
        start_date = datetime.now() - timedelta(days=30)
        period_name = 'Son 30 Gün'
    elif date_filter == '90':
        start_date = datetime.now() - timedelta(days=90)
        period_name = 'Son 90 Gün'
    else:
        start_date = None
        period_name = 'Tüm Zamanlar'
    
    # Genel istatistikler
    total_products = Product.objects.filter(is_active=True).count()
    total_value = Product.objects.filter(is_active=True).aggregate(
        total=Sum(F('quantity') * F('unit_price'))
    )['total'] or 0
    
    # Kategori bazlı analiz
    category_stats = Category.objects.annotate(
        product_count=Count('products'),
        total_quantity=Sum('products__quantity'),
        total_value=Sum(F('products__quantity') * F('products__unit_price'))
    ).order_by('-total_value')
    
    # Stok hareketleri özeti
    movements_query = StockMovement.objects.all()
    if start_date:
        movements_query = movements_query.filter(created_at__gte=start_date)
    
    total_in = movements_query.filter(movement_type='IN').aggregate(total=Sum('quantity'))['total'] or 0
    total_out = movements_query.filter(movement_type='OUT').aggregate(total=Sum('quantity'))['total'] or 0
    
    # En çok hareket gören ürünler
    top_movements = Product.objects.annotate(
        movement_count=Count('movements')
    ).filter(movement_count__gt=0).order_by('-movement_count')[:10]
    
    context = {
        'total_products': total_products,
        'total_value': total_value,
        'category_stats': category_stats,
        'total_in': total_in,
        'total_out': total_out,
        'top_movements': top_movements,
        'period_name': period_name,
        'date_filter': date_filter,
    }
    return render(request, 'inventory/reports.html', context)
