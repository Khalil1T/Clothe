from django.urls import path

from .views import home, ProdcutDetailView

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', ProdcutDetailView.as_view(), name='product-detail'),
    ]