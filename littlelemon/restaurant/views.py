from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Little Lemon Restaurant")

def add_item(request):
    add_item = Menu.objects.create(
        name="cottage pie",
        description="A delicious cottage pie",
        price=9.99,
        available=True)
    return HttpResponse("Added Item")

def menu(request):
    menu_item = Menu.objects.all()
    return render(request, 'menu.html', {'menu' : menu_item })

