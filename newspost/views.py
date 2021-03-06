from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import News,Category,Tag
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import NewsCategoryForm,NewsForm,NewsTagForm


@login_required(login_url='signin')
def list_category(request):
    data = Category.objects.all()[::-1]
    context = {
        'categories': data
    }
    return render(request, 'backend/category/list.html', context)

@login_required(login_url='signin')
def create_category(request):
    form = NewsCategoryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Category added successfully")
        return redirect('category')
    context = {
        'forms': form
    }
    return render(request, 'backend/category/create.html', context)

@login_required(login_url='signin')
def edit_category(request, id):
    data = Category.objects.get(pk=id)
    form = NewsCategoryForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Category updated successfully")
        return redirect('category')
    context = {
        'forms': form

    }
    return render(request, 'backend/category/edit.html', context)

@login_required(login_url='signin')
def delete_category(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, "Category successfully deleted")
    return redirect('category')

@login_required(login_url='signin')
def list_news(request):
    data = News.objects.all()[::-1]
    context = {
        'news': data
    }
    return render(request, 'backend/news/list.html', context)

@login_required(login_url='signin')
def create_news(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "News added successfully")
        return redirect('news')
    context = {
        'forms': form
    }
    return render(request, 'backend/news/create.html', context)

@login_required(login_url='signin')
def edit_news(request, id):
    data = News.objects.get(pk=id)
    form = NewsForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "News updated successfully")
        return redirect('news')
    context = {
        'forms': form

    }
    return render(request, 'backend/news/edit.html', context)

@login_required(login_url='signin')
def delete_news(request, id):
    news = News.objects.get(pk=id)
    news.delete()
    messages.add_message(request, messages.SUCCESS, "News successfully deleted")
    return redirect('news')


@login_required(login_url='signin')
def list_tag(request):
    data = Tag.objects.all()[::-1]
    context = {
        'tags': data
    }
    return render(request, 'backend/tag/list.html', context)

@login_required(login_url='signin')
def create_tag(request):
    form = NewsTagForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Tag added successfully")
        return redirect('tag')
    context = {
        'forms': form
    }
    return render(request, 'backend/tag/create.html', context)

@login_required(login_url='signin')
def edit_tag(request, id):
    data = Tag.objects.get(pk=id)
    form = NewsTagForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Tag updated successfully")
        return redirect('tag')
    context = {
        'forms': form

    }
    return render(request, 'backend/tag/edit.html', context)

@login_required(login_url='signin')
def delete_tag(request, id):
    data = Tag.objects.get(pk=id)
    data.delete()
    messages.add_message(request, messages.SUCCESS, "News successfully deleted")
    return redirect('tag')
