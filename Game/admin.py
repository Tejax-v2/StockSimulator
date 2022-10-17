from django.contrib import admin
from .models import Game

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ['id','date','start_time','end_time','is_live','is_completed','is_cancelled']
    
admin.site.register(Game,GameAdmin)