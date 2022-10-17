from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('is_live/', views.check_if_live,name='home'),
]