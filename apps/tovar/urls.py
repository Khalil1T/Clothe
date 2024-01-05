from django.urls import path

from .views import home, ProdcutDetailView, contact, collection

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', ProdcutDetailView.as_view(), name='product-detail'),
    path('contact/', contact, name='contact'),
    path('collection/', collection, name='collection')
    ]