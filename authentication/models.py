from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_Info(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    total_amt = models.IntegerField(default=100) #default is the initial balance of each player

    def __str__(self):
        return self.name
    