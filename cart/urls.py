from django.urls import path
from .views import add_cart,sub_cart,remove_cart,cart

urlpatterns = [
    path('', cart, name="cart"),
    path('add_product/<int:product_id>/', add_cart, name="cart_add"),
    path('sub_product/<int:product_id>/', sub_cart, name="cart_sub"),
    path('remove_product/<int:product_id>/', remove_cart, name="cart_remove")
]