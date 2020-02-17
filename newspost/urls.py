from django.urls import path
from . import views

urlpatterns = [
    path('category/',views.list_category,name='category'),
    path('category/create/',views.create_category,name='create_category'),
    path('category/delete/<int:id>',views.delete_category,name='delete_category'),
    path('category/edit/<int:id>',views.edit_category,name='edit_category'),

    path('news/',views.list_news,name='news'),
    path('news/create/',views.create_news,name='create_news'),
    path('news/delete/<int:id>',views.delete_news,name='delete_news'),
    path('news/edit/<int:id>',views.edit_news,name='edit_news'),

]