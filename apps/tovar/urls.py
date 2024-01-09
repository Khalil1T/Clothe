from django.urls import path

from . import views
from .views import home, ProdcutDetailView, Search

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', ProdcutDetailView.as_view(), name='product-detail'),
    path('search/', Search.as_view(), name='search'),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]