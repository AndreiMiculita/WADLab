from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

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

    if request.user.is_authenticated():
        user = request.user
    amount = request.POST['amount']
    address = request.POST['address']
    comments = request.POST['comments']
    try:
        neworder = Order(address=address, customer_comment=comments, time_placed=timezone.now(), product=product,
                         amount=amount, customer=user)
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


def orders(request):
    if request.user.is_authenticated():
        user = request.user
    order_list = Order.objects.filter(customer_id=user.id)
    context = {'order_list': order_list}
    return render(request, 'pizza/order.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request   )
            return render(request, 'pizza/order.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def placeorder(request, order_id):
    o = get_object_or_404(Order, id=order_id)
    o.state = "OR"
    o.save()
    return HttpResponseRedirect(reverse('pizza:orders'))


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('pizza:orders')
