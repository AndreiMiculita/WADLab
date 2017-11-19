from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Product, Choice, Order


def index(request):
    return render(request, 'pizza/index.html')


def contact(request):
    return render(request, 'pizza/contact.html')


def about(request):
    return render(request, 'pizza/about.html')


def menu(request):
    latest_product_list = Product.objects.order_by('-pub_date')[:5]
    context = {'latest_product_list': latest_product_list}
    return render(request, 'pizza/menu.html', context)


def detail(request, linkstr):
    product = get_object_or_404(Product, link_str=linkstr)
    return render(request, 'pizza/detail.html', {'product': product})


def addchoice(request, linkstr):
    choice = Choice(product=Product.objects.get(pk=1 ), amount=1, order=Order.objects.get(pk=1))
    choice.save()
    try:
        order = Order.objects.get(pk=1)
    except (KeyError, Order.DoesNotExist):
        return render(request, 'pizza/detail.html', {
            'product': choice.product,
            'error_message': "whoops",
        })
    else:
        order.choice_set.add(choice)
        order.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('menu'))
