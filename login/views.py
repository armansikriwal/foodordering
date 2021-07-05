from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

from django.views import View
# Create your views here.


class Signup(View):
    def post(self,request):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists(): 
                messages.info(request," email already exists")
                return redirect("register")

            else:
                user= User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect("/")
        else :
            messages.info(request,"password doesnt match")
            return redirect("register")
        return redirect("/")
    
    def get(self,request):
        return render(request,"register.html")

        

class Login(View):
    return_url= None
    def get(self,request):
        Login.return_url=request.GET.get('return_url')
        return render(request,"login.html")
    
    def post(self,request):
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request.session['username']=user.username
            if Login.return_url :
                login(request,user)
                return HttpResponseRedirect(Login.return_url)
            else:
                Login.return_url=None
                login(request,user)
                return redirect("/")
        else:
            messages.info(request,"enter valid details")
            return redirect("login")



        

    
def logout_view(request):
    logout(request)
    return redirect("/")
