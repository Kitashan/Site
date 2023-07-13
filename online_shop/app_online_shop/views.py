from django.shortcuts import render
# объект для https запроса
from django.http import HttpResponse

# Create your views here.

# Функция отображающая файл index.html
def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advert(request):
    return render(request, 'advertisement.html')

def advert_post(request):
    return render(request, 'advertisement-post.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')