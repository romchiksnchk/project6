import password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
