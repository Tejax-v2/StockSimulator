from django.contrib import admin
from .models import User_Info

# Register your models here.

class User_Info_Admin(admin.ModelAdmin):
    list_display = ['user_id','name','contact','total_amt','session_id']

admin.site.register(User_Info,User_Info_Admin)