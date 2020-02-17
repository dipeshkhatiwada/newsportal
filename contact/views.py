from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ContactForm


@login_required(login_url='signin')
def list_contact(request):
    data = Contact.objects.all().order_by('status')
    context = {
        'messages': data
    }
    return render(request, 'backend/message/list.html', context)

def detail_contact(request, id):
    data = Contact.objects.get(pk=id)
    data.status=True
    data.save()
    # form = ContactForm(request.POST or None, request.FILES or None, instance=data)
    # if form.is_valid():
    #     form.save()
    #     messages.add_message(request, messages.SUCCESS, "Message updated successfully")
    #     return redirect('contact')
    context = {
        'message': data,


    }
    return render(request, 'backend/message/detail.html', context)


def delete_contact(request, id):
    contact = Contact.objects.get(pk=id)
    contact.delete()
    messages.add_message(request, messages.SUCCESS, "Message successfully deleted")
    return redirect('message')


