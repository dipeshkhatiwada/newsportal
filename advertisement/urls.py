from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_advertisement,name='advertisement'),
    path('create',views.create_advertisement,name='create_advertisement'),
    path('delete/<int:id>',views.delete_advertisement,name='delete_advertisement'),
    path('edit/<int:id>',views.edit_advertisement,name='edit_advertisement'),
]