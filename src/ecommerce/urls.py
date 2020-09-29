from django.urls import path
from .views import home, checkout, products

app_name = "ecommerce"


urlpatterns = [
    path("", home, name="home"),
    path("checkout/", checkout, name="checkout"),
    path("products/", products, name="products"),
]
