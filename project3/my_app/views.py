from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Test heading in the first test view</h1>")


def deep_learning(request):
    return HttpResponse("welcome to our deep learning course")
def deep_learning(request):
    return HttpResponse("welcome to our machine learning course")
