from django.urls import path
from .views import Index, Cart,Checkout
urlpatterns = [
    path("",Index.as_view(),name="index"),
    path("cart",Cart.as_view(),name="cart"),
    path("checkout",Checkout.as_view(),name="checkout"),
]
