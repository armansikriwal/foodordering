from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from .models import Order, Product , Category
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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

class Checkout(View):
    def post(self,request):
        address= request.POST.get("address")
        phone= request.POST.get("phone")
        customer=request.user.id
        cart=request.session.get("cart")
        products= Product.get_by_ids(list(cart.keys()))
        for product in products:
            order=Order (customer=User(id=customer) ,
            product=product,
            price=product.price,
            address=address,
            phone_num=phone ,
            quantity=cart.get(str(product.id))
             )
            order.place_order()
            request.session['cart']={}

        return redirect('cart')

class OrderView(View):
    def get(self,request):
        customer=request.user.id
        orders=Order.get_orders_of_user(customer)
        #print(orders)
        return render(request,"orders.html",{'orders':orders})

