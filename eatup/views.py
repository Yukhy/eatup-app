from django.shortcuts import render, redirect
from pos.models import *
from accounts.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ScanItemForm, AddCartForm

# Create your views here.

TAX = 0.08

def index(request):
    return render(request, 'eatup/index.html')

@login_required
def shopping_cart(request):
    cart = Cart.objects.filter(user=request.user, is_checked_out=False)
    subtotal = 0
    for item in cart:
        for pos in item.pos.all():
            subtotal += pos.price * item.count
    params = {
        'cart': cart,
        'subtotal': subtotal,
        'tax': TAX * 100,
        'total': int(subtotal * (1 + TAX)),
    }
    if request.method == 'POST':
        for cart in cart:
            cart.is_checked_out = True
            cart.save()
        return redirect('eatup:index')
    return render(request, 'eatup/shoppingcart.html', params)

@login_required
def notification(request):
    history = Cart.objects.filter(user=request.user, is_checked_out=True)
    params = {
        'history': history,
    }
    return render(request, 'eatup/notification.html', params)

@login_required
def user_info(request):
    user = User.objects.get(username=request.user)
    params = {
        'user': user,
    }
    return render(request, 'eatup/usermenu.html', params)

@login_required
def scan(request):
    form = ScanItemForm()
    params = {
        'form': form,
    }
    return render(request, 'eatup/scan.html', params)

# api

def api_scan_item(request):
    pos_id = request.POST.get('pos_id')
    get_pos = Pos.objects.get(pos_number=pos_id)
    cart = Cart.objects.create(user=request.user)
    cart.pos.add(get_pos)

    return redirect('eatup:shopping-cart')