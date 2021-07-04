from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from .models import Product , Category
# Create your views here.

def index(request):
    products=None
    categorys=Category.get_all_category()
    Category_id=request.GET.get("category")
    if Category_id:
        products=Product.get_by_id(Category_id)
    else:
        products=Product.get_all_products()
    context={"products":products,"categorys":categorys}
    
    return render(request,"index.html",context)