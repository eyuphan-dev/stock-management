from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('urun/<int:pk>/', views.product_detail, name='product_detail'),
    path('urun/ekle/', views.product_create, name='product_create'),
    path('urun/<int:pk>/duzenle/', views.product_update, name='product_update'),
    path('urun/<int:pk>/sil/', views.product_delete, name='product_delete'),
    path('kategoriler/', views.category_list, name='category_list'),
    path('kategori/ekle/', views.category_create, name='category_create'),
    path('raporlar/', views.reports, name='reports'),
]
