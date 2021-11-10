from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'eatup/index.html')

def shopping_cart(request):
    return render(request, 'eatup/shoppingcart.html')

def notification(request):
    return render(request, 'eatup/notification.html')

def user_info(request):
    return render(request, 'eatup/usermenu.html')

def scan(request):
    return render(request, 'eatup/scan.html')