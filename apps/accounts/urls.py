from django.urls import path

from apps.accounts.views import register

urlpatterns = [
    path('register/', register, name='register')
]