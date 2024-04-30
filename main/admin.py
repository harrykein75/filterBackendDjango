from django.contrib import admin
from .models import *

# Register your models here.
class PointAdmin(admin.ModelAdmin):
    list_display = ('location','address','user','latitude','longitude','visible','date')
    #fields,  fieldsets, inlines list_filter search_fields 

admin.site.register(Point, PointAdmin)