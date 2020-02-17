from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from newspost.models import Category,News
from contact.models import Contact
from contact.forms import ContactForm
from django.db.models import Sum, Count
import requests


def contact(request):
    data = Category.objects.filter(status=1, menu_display=1)
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "सन्देश सफलतापूर्वक सबमिट गरियो")
        return redirect('contact')
    context = {
        'categories': data,
        'forms': form
    }
    return render(request, 'contact.html',context)


def home(request):
    data = Category.objects.filter(status=1, menu_display=1)
    sliders = News.objects.filter(status=1,slider=1).order_by('-publish_date')
    main_news = News.objects.filter(status=1,main_news=1).order_by('-publish_date')
    main_news1 = main_news.first()
    main_news=main_news[1:3]
    cat1_news = News.objects.filter(category_id=1,status=1).order_by('-publish_date')
    context = {
        'categories': data,
        'sliders': sliders,
        'main_news': main_news,
        'main_news1': main_news1,
        'cat1_news': cat1_news,
    }
    return render(request, 'home.html', context)


def category(request,slug):
    data = Category.objects.filter(status=1, menu_display=1)
    cat = Category.objects.get(slug=slug)
    news = News.objects.filter(category_id=cat.id, status=1)
    context = {
        'categories': data,
        'cat':cat.title,
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





def signin(request):
    if request.method == 'GET':
        return render(request, 'backend/login.html')
    else:
        u = request.POST.get('username')
        # u = request.POST['username']
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            # messages.add_message(request, messages.SUCCESS, "Login success")
            return redirect("dashboard")
        else:
            messages.add_message(request, messages.ERROR, "Username and Password doesn't match")
            return redirect("signin")

        # else:
        #     return HttpResponse("Password Error")


def signout(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def list_user(request):
    data = User.objects.all()[::-1]
    context = {
        'users': data
    }
    return render(request, 'backend/user/list.html', context)
def add_user(request):
    if request.method == 'GET':
        return render(request, 'backend/user/create.html')
    else:
        f = request.POST.get('first_name')
        l = request.POST.get('last_name')
        u = request.POST.get('username')
        # u = request.POST['username']
        e = request.POST.get('email')
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if p1 == p2:
            try:
                u = User(first_name=f, last_name=l ,username=u, email=e)
                u.set_password(p1)
                u.save()
            except:
                messages.add_message(request, messages.ERROR, "Username already exists")
                return redirect("create_user")
            messages.add_message(request, messages.SUCCESS, "User added successfully")
            return redirect("user")
        else:
            messages.add_message(request, messages.ERROR, "Password doesn't match")
            return redirect("create_user")
def edit_user(request,id):
    if request.method == 'GET':
        data = User.objects.get(pk=id)
        context = {
            'user': data
        }
        return render(request, 'backend/user/edit.html',context)
    else:
        f = request.POST.get('first_name')
        l = request.POST.get('last_name')
        e = request.POST.get('email')
        data = User.objects.get(pk=id)
        data.first_name = f
        data.last_name = l
        data.email = e
        data.save()
        messages.add_message(request, messages.SUCCESS, "user updated successfully")
        return redirect("user")



def dashboard(request):
    no_user = User.objects.filter(is_active=True).aggregate(Count('id'))
    no_message = Contact.objects.filter(status=False).aggregate(Count('id'))
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7d043da1b183b31c5cba4e3d65d9ccec'
    city = 'kathmandu'
    city_weather = requests.get(url.format(city)).json() 
    #request the API data and convert the JSON to Python data types
    weather = {
        'city' : city,
        'temperature' : round((city_weather['main']['feels_like']- 32)*5/9,2) ,
        'min_temp' : round((city_weather['main']['temp_min']- 32)*5/9,2) ,
        'max_temp' : round((city_weather['main']['temp_max']- 32)*5/9,2) ,
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    
    context = {
        'no_user': no_user,
        'no_message': no_message,
        'weather':weather,
    }
    return render(request, 'backend/dashboard.html',context)



