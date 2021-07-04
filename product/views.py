from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from .models import Product , Category
from django.views import View
# Create your views here.

class Index(View):
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products=None
        categorys=Category.get_all_category()
        Category_id=request.GET.get("category")
        print(Category_id)
        if Category_id:
            products=Product.get_by_id(Category_id)
        else:
            products=Product.get_all_products()
        context={"products":products,"categorys":categorys}
        #print('you are : ',request.session.get("username"))
        return render(request,"index.html",context)

    def post(self,request):
        product=request.POST.get("product")
        remove=request.POST.get("remove")
        
        cart=request.session.get('cart')
        if cart :
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity -1
                else:
                    cart[product]=quantity +1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        
        request.session['cart']=cart
        print(request.session['cart'])
        return redirect("/")

class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_by_ids(ids)
        return render(request,"cart.html",{'products':products})

