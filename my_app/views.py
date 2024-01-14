from django.http import HttpResponse
from django.shortcuts import render


def home1(request):
    return HttpResponse("<h1>Hello this is home 1.</h1>")


def home2(request):
    return HttpResponse("<h2>This is home 2.</h2>")

def home3(request):
    return HttpResponse("<h3>This is home 3.</h3>")


def template_home(request):
    return render(request, template_name="my_app/home.html")


def template_home2(request):
    return render(request, template_name="my_app/newHome.html")