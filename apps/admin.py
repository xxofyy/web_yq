from django.contrib import admin
from apps.models import AppName

# Register your models here.

@admin.register(AppName)
class AppNameadmin(admin.ModelAdmin):
    list_display = ('id','app_name','app_href')