
from django.urls import path
from main.views import IndexPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index')
    
]
