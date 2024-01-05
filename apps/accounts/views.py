from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.accounts.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
    products = Product.objects.filter(author=request.user)
    return render(request, 'accounts/profile.html', {'products': products})


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'accounts/update_profile.html', context)



def profile_detail(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, 'accounts/profile_detail.html', {'profile': profile})