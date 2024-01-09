import self
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import ListView

from .models import Product
from .forms import ReviewForm


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', context={'products': products})


class ProdcutDetailView(generic.DetailView):
    model = Product
    template_name = 'product/product_detail.html'


class Search(ListView):
    paginate_by = 3
    template_name = 'product/product_list.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Product.objects.filter(name__icontains=query)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context

class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = product
            review.save()
        return redirect(product.get_absolute_url())



