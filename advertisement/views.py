from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Advertisement
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import AdvertisementForm


@login_required(login_url='signin')
def list_advertisement(request):
    data = Advertisement.objects.all()[::-1]
    context = {
        'advertisements': data
    }
    return render(request, 'backend/advertisement/list.html', context)


def create_advertisement(request):
    form = AdvertisementForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Advertisement added successfully")
        return redirect('advertisement')
    context = {
        'forms': form
    }
    return render(request, 'backend/advertisement/create.html', context)


def edit_advertisement(request, id):
    data = Advertisement.objects.get(pk=id)
    form = AdvertisementForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Advertisement updated successfully")
        return redirect('advertisement')
    context = {
        'forms': form

    }
    return render(request, 'backend/advertisement/edit.html', context)


def delete_advertisement(request, id):
    advertisement = Advertisement.objects.get(pk=id)
    advertisement.delete()
    messages.add_message(request, messages.SUCCESS, "advertisement successfully deleted")
    return redirect('advertisement')
