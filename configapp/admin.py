from django.contrib import admin

from .models import *

class studentAdmin(admin.ModelAdmin):
    list_display = ('kurs','full_name','phone','email')
    list_display_links = ['full_name']
    search_fields = ['full_name','kurs']
    list_editable = ['phone']

class kursAdmin(admin.ModelAdmin):
    list_display = ('title','boshlanish','tugashi')
    list_display_links = ['title']
    search_fields = ['title']

admin.site.register(Student,studentAdmin)
admin.site.register(Kurs,kursAdmin)
