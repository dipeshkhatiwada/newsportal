from django.contrib import admin
from .models import Advertisement
from django import forms

# Register your models here.

class AdvertisementForm(admin.ModelAdmin):
    
    list_display = ('link', 'image','status',)
    list_filter = ('status',)
    search_fields = ('link', 'image','status',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('link', 'image','status',),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('link', 'image','status',),
        }),
    )

    filter_horizontal = []
    ordering = ('-link',)
    list_per_page = 5
   

admin.site.register(Advertisement,AdvertisementForm)