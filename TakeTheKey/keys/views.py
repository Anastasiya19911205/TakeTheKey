from django.shortcuts import render
from django.http import HttpResponse

def key (request):
    return render(request, "key.html")

def activate (request):
    return render(request, "activate.html")

def feedback (request):
    return render(request, "feedback.html")

