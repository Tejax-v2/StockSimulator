from django.contrib import admin
from .models import Stock

# Register your models here.

class Stocks_Admin(admin.ModelAdmin):
    list_display = ['name','price']

admin.site.register(Stock,Stocks_Admin)