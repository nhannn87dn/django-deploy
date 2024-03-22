from django.urls import path
from . import views

urlpatterns = [
    path("", views.cartList, name="cart-list"),
    path("checkout/", views.cartCheckout, name="cart-checkout"),
    path("thanks/", views.cartThanks, name="cart-thanks"),
    path("add-item/", views.add_to_cart, name="cart-add"),
    path("increase-quantity/", views.increase_quantity, name="cart-increase"),
    path("decrease-quantity/", views.decrease_quantity, name="cart-decrease"),
]
