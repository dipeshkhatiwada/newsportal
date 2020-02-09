from django.contrib import admin
from .models import Category,News
from django import forms

# Register your models here.

class CategoryForm(admin.ModelAdmin):
    
    list_display = ('title', 'status','menu_display')
    list_filter = ('status','menu_display')
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'slug','status', 'menu_display',),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'slug','status', 'menu_display',),
        }),
    )

    filter_horizontal = []
    ordering = ('-title',)
    list_per_page = 5
   
class NewsForm(admin.ModelAdmin):
    
    list_display = ('title', 'category', 'status','view_count')
    list_filter = ('status',)
    search_fields = ('title','category',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('category', 'title', 'slug','image','description','status', ),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('category', 'title', 'slug','image','description', 'status', ),
        }),
    )

    filter_horizontal = []
    ordering = ('-publish_date',)
    list_per_page = 10
    

admin.site.register(Category,CategoryForm)
admin.site.register(News, NewsForm)