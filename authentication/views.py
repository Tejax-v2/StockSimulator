import datetime
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
import jwt
# Create your views here.

#CBV for signup
class SignUpView(View):
    def get(self,request):  #on get request user will get signup form 
        return render(request,'signup.html')
    def post(self,request):  #on submitting the signup form data will be fetched from request
        username = request.POST.get('username')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:  #checks if password and confirm password are same
            if User.objects.filter(username=username).exists():  #checks if username is already taken
                return render(request,'signup.html',{'error':'Username already exists'})
            else:
                user = User.objects.create_user(username=username,password=pass1)  #register the new user
                user.save()
                user_info = User_Info.objects.create(user_id=user,name=name,contact=contact)  #register the extra user data
                user_info.save()
                return redirect('signin')  #After successful signup user will be redirected to signin
        else:
            return render(request,'signup.html',{'error':'Passwords do not match'})  #if password and confirm password don't match

#CBV for signin
class SignInView(View):
    def get(self,request):  #on get request user will get signup form 
        return render(request,'signin.html')
    def post(self,request):  #Getting data from submitted form
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)  
        if user is not None:  #if user gets authenticated
            login(request,user)
            #dictionary named payload to be encoded into cookie
            payload = {
                "username" : user.get_username(),
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                "iat": datetime.datetime.utcnow()
            }
            token = jwt.encode(payload,'antaptii',algorithm='HS256') #payload encoded into cookie
            response = HttpResponseRedirect('/',{'user':user})  #redirects to home
            response.data = { "success" : True , "user":user}
            response.set_cookie(key='token', value=token, httponly=True)  
            # code for linking cookie
            return response
        else:
            return render(request,'signin.html',{"error":"Invalid Credentials"})

#CBV for signout
class SignOutView(View):
    def get(self,request):
        logout(request)
        return redirect('signin') #after logging out signin form will be shown