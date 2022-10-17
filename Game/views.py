from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def check_if_live(request):
    if request.method=="GET":
        game_id='619'
        is_live=True
        return JsonResponse({'game_id':game_id,'is_live':is_live})
