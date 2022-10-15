from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
import jwt
from authentication.models import User_Info

class HomeView(View):
    def get(self,request):
        try:
            username = request.session.get('username')  #get username from session id
            myuser = User.objects.get(username=username)  #get the user object
            user_info = User_Info.objects.get(user_id=myuser)  #get the user_info object
            if(user_info.session_id == request.session.session_key):  #if session key in cookies matches the session key in database
                getuser = User.objects.get(username=username)  #getting user from database
                return render(request,'index.html',{'getuser':getuser})  #returns signin page with user
            else:
                return render(request,'index.html',{'error':'Please Sign In'})
        except:  
            return render(request,'index.html',{'error':'Please Sign In'})

