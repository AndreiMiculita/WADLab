from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from .models import Product, Order


def index(request):
    return render(request, 'pizza/index.html')


def contact(request):
    return render(request, 'pizza/contact.html')


def about(request):
    return render(request, 'pizza/about.html')


def menu(request):
    latest_product_list = Product.objects.order_by('-pub_date')
    context = {'latest_product_list': latest_product_list}
    return render(request, 'pizza/menu.html', context)


def detail(request, linkstr):
    product = get_object_or_404(Product, link_str=linkstr)
    return render(request, 'pizza/detail.html', {'product': product})


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('pizza:menu'))
    else:
        return HttpResponseRedirect(reverse('pizza:contact'))


def logout(request):
    logout(request)
    return redirect('pizza:contact')


def addorder(request, linkstr):
    product = get_object_or_404(Product, link_str=linkstr)
    try:
        neworder = Order(address='someaddress',  customer_comment='spicy', time_placed=timezone.now(), product=product,
                      amount=1)
    except (KeyError, Order.DoesNotExist):
        return render(request, 'pizza/detail.html', {
            'product': product,
            'error_message': "No order exists",
        })
    else:
        neworder.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('pizza:menu'))


def order(request):
    order_list = Order.objects.all()
    context = {'order_list': order_list}
    return render(request, 'pizza/order.html', context)