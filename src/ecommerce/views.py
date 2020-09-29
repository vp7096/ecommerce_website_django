from django.shortcuts import render
from .models import Item, OrderItem, Order


def home(request):
    context = {"items": Item.objects.all()}
    return render(request, "ecommerce/home_page.html", context)


def checkout(request):
    return render(request, "ecommerce/checkout_page.html")


def products(request):
    return render(request, "ecommerce/product-page.html")