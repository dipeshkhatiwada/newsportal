from django.urls import path
from . import views

urlpatterns = [
    path('/',views.list_contact,name='message'),
    path('delete/<int:id>',views.delete_contact,name='delete_message'),
    path('details/<int:id>',views.detail_contact,name='detail_message'),

  
]