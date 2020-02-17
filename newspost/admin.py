from django.contrib import admin
from .models import Category,News
from django import forms

# Register your models here.

class CategoryForm(admin.ModelAdmin):
    
    list_display = ('title', 'status','menu_display','rank')
    list_filter = ('status','menu_display',)
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'slug','status', 'menu_display','rank'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'slug','status', 'menu_display','rank'),
        }),
    )

    filter_horizontal = []
    ordering = ('-title','-rank',)
    list_per_page = 5
   
class NewsForm(admin.ModelAdmin):
    
    list_display = ('title', 'category', 'status','main_news','slider','view_count')
    list_filter = ('status','main_news','slider',)
    search_fields = ('title','category',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('category', 'title', 'slug','image','description','main_news','slider', 'status', ),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('category', 'title', 'slug','image','description','main_news','slider', 'status', ),
        }),
    )

    filter_horizontal = []
    ordering = ('-publish_date',)
    list_per_page = 10
    

admin.site.register(Category,CategoryForm)
admin.site.register(News, NewsForm)