from django.contrib import admin
from .models import User_Stock

# Register your models here.

class User_Stocks_Admin(admin.ModelAdmin):
    list_display = ['user_id','stock_id','quantity']

admin.site.register(User_Stock,User_Stocks_Admin)