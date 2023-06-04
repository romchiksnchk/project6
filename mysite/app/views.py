from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import ProductForm
from .models import Product
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


class Index(TemplateView):
    template_name = 'index.html'


class Product(ListView):
    model = Product
    template_name = 'product.html'


class About(TemplateView):
    template_name = 'about.html'


class Contact(TemplateView):
    template_name = 'contact.html'


class AddProduct(LoginRequiredMixin, CreateView):
    template_name = 'add_product.html'
    model = Product
    login_url = '/login'
    success_url = '/product'
    form_class = ProductForm


class Login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('index')

class Register(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))