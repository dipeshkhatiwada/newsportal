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


    path('tag/',views.list_tag,name='tag'),
    path('tag/create/',views.create_tag,name='create_tag'),
    path('tag/delete/<int:id>',views.delete_tag,name='delete_tag'),
    path('tag/edit/<int:id>',views.edit_tag,name='edit_tag'),

]