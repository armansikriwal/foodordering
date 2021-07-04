from django.urls import path
from .views import Index, Cart
urlpatterns = [
    path("",Index.as_view(),name="index"),
    path("cart",Cart.as_view(),name="cart")
]
