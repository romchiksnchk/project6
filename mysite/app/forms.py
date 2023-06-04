from msilib.schema import Class

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User

from .models import Product
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password')