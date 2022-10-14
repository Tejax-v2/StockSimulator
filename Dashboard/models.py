from django.db import models
from authentication.models import User_Info
from Stocks.models import Stock

# Create your models here.

class User_Stock(models.Model):
    user_id = models.ForeignKey(User_Info, on_delete=models.CASCADE)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
