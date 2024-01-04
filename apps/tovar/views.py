from django.shortcuts import render
from django.views import generic

from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', context={'products': products})


class ProdcutDetailView(generic.DetailView):
    model = Product
    template_name = 'product/product-detail.html'
