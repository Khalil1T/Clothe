from django.urls import path

from . import views
from .views import home, ProdcutDetailView

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', ProdcutDetailView.as_view(), name='product-detail'),
    path('search/', views.Search.as_view(), name='search')
    ]