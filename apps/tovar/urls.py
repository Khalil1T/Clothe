from django.urls import path

from .views import home, ProdcutDetailView, Search

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', ProdcutDetailView.as_view(), name='product-detail'),
    path('search/', Search.as_view(), name='search')
    ]