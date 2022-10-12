from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class SignUpView(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        username = request.POST.get('username')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                return render(request,'signup.html',{'error':'Username already exists'})
            else:
                user = User.objects.create_user(username=username,password=pass1)
                user.save()
                user_info = User_Info.objects.create(user_id=user,name=name,contact=contact)
                user_info.save()
                return redirect('signin')
        else:
            return render(request,'signup.html',{'error':'Passwords do not match'})

class SignInView(View):
    def get(self,request):
        return render(request,'signin.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'signin.html',{'error':'Invalid Credentials'})

class SignOutView(View):
    def get(self,request):
        logout(request)
        return redirect('signin')