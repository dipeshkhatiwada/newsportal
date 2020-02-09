from django.shortcuts import render
from newspost.models import Category,News


def about(request):
    return render(request, 'about.html')


def home(request):
    data = Category.objects.filter(status=1, menu_display=1)
    context = {
        'categories': data
    }
    return render(request, 'home.html', context)


def category(request,slug):
    data = Category.objects.filter(status=1, menu_display=1)
    cat = Category.objects.get(slug=slug)
    news = News.objects.filter(category_id=cat.id, status=1)
    context = {
        'categories': data,
        'news': news
    }
    return render(request, 'category.html', context)
def news(request,slug):
    data = Category.objects.filter(status=1, menu_display=1)
    news = News.objects.get(slug=slug)
    context = {
        'categories': data,
        'news': news
    }
    return render(request, 'news.html', context)