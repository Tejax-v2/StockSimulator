from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
import jwt

class HomeView(View):
    def get(self,request):
        token = request.COOKIES.get('token')  #check if there is any cookie stored in browser
        if token==None:  
            return render(request,'index.html',{'error':'Please Sign In'})
        else:  #if cookie found
            try:
                payload = jwt.decode(token, "antaptii", algorithms = 'HS256')  #decoding cookie
            except:
                return render(request,'index.html',{'error':'Please Sign In'})
            user = User.objects.get(username=payload['username'])  #getting logged in user
            return render(request,'index.html',{'user':user})

