from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.accounts.forms import UserRegisterForm
from .models import Profile
from ..tovar.models import Product


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Wellcome {username}')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def teachers(request):
    profiles = Profile.objects.all()
    return render(request, 'accounts/teachers.html', context={'profiles': profiles})


@login_required
def profile(request):
    products = Product.objects.filter(brand=request.user)
    return render(request, 'accounts/profile.html', {'products': products})



def profile_detail(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, 'accounts/profile_detail.html', {'profile': profile})

