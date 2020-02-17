from django.contrib import admin
from .models import Contact
from django import forms

# Register your models here.
class ContactForm(admin.ModelAdmin):
    
    list_display = ('name', 'email', 'subject','status')
    list_filter = ('status',)
    search_fields = ('name','email',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email','subject','message', 'status', ),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'name', 'email','subject','message', 'status', ),
        }),
    )
    edit_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'name', 'email','subject', ),
        }),
    )

    filter_horizontal = []
    ordering = ('-date',)
    list_per_page = 10
    

admin.site.register(Contact,ContactForm)