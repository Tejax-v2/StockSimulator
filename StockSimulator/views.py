from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
import jwt

class HomeView(View):
    def get(self,request):
        token = request.COOKIES.get('token')
        if token==None:
            return render(request,'index.html',{'error':'Please Sign In'})
        else:
            try:
                payload = jwt.decode(token, "antaptii", algorithms = 'HS256')
            except:
                return render(request,'index.html',{'error':'Please Sign In'})
            user = User.objects.get(username=payload['username'])
            return render(request,'index.html',{'user':user})

