from django.shortcuts import render, redirect
from web.models import Product
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from cart.forms import CartAddProductForm
from django.db.models import Q

def index(request):
    return render(request, 'web/index.html')

def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render (request, 'web/shop.html', context)

def about(request):
    return render (request, 'web/about.html')

def partner(request):
    return render (request, 'web/partner.html')

def diplomi(request):
    return render (request, 'web/diplomi.html')

def innovations(request):
    return render (request, 'web/innovations.html')

def postavshiki(request):
    return render (request, 'web/postavshiki.html')

def medkab(request):
    return render (request, 'web/medkab.html')

def sanit(request):
    return render (request, 'web/sanit.html')

class tovar(DetailView):
    model = Product
    template_name = 'web/tovar.html'
    slug_field = "id"

def product_detail (request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'web/tovar.html', {'product': product, 'cart_product_form': cart_product_form})
