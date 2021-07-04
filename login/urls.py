from django.shortcuts import render
from django.urls import path
from .views import Login,Signup
from . import views

urlpatterns = [
    path("signup", Signup.as_view(), name="register"),
    path("login", Login.as_view(), name="login"),
    path("logout", views.logout_view, name="logout"),
    

]
