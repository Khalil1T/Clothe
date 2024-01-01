from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user_default.jpeg', upload_to='profile_images')

    def __str__(self):
        return self.user.username
