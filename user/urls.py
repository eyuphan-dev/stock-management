from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('giris/', views.login_view, name='login'),
    path('cikis/', views.logout_view, name='logout'),
    path('kayit/', views.register_view, name='register'),
]
