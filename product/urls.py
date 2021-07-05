from django.urls import path
from .views import Index, Cart,Checkout , OrderView
from middlewares.auth import auth_middleware


urlpatterns = [
    path("",Index.as_view(),name="index"),
    path("cart",Cart.as_view(),name="cart"),
    path("checkout",Checkout.as_view(),name="checkout"),
    path("orders",auth_middleware(OrderView.as_view()),name="orders"),

]
