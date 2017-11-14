from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'pizza/index.html')


def contact(request):
    return render(request, 'pizza/contact.html')


def about(request):
    return render(request, 'pizza/about.html')


def menu(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'pizza/menu.html', context)


def detail(request, linkstr):
    question = get_object_or_404(Question, link_str=linkstr)
    return render(request, 'pizza/detail.html', {'question': question})
