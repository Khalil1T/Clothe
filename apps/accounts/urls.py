from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register, profile, profile_detail, teachers

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        success_url='profile'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('teachers/', teachers, name='teachers'),
    path('profile/<int:pk>', profile_detail, name='profile-detail'),
]