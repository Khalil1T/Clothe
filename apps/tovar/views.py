from django.shortcuts import render, redirect
from django.views import generic, View
from django.views.generic import ListView

from .models import Product
from .forms import ReviewForm


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', context={'products': products})


class ProdcutDetailView(generic.DetailView):
    model = Product
    template_name = 'product/product-detail.html'


class Search(ListView):
    template_name = 'base.html'
    context_object_name = 'product'
    paginate_by = 5
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(name__icontains=query)
        else:
            return Product.objects.all()
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

class AddReview(View):
    def post(self, requset, pk):
        form = ReviewForm(requset.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = product
            form.save()
        # return redirect(product.get_absolute_url)
        # return redirect("/")
        return redirect('name_of_the_view_for_movie_details', product_id=movie_id)