from django.shortcuts import render
from django.http import HttpResponse

def key (request):
    return HttpResponse(f"<h1> On-line активация приобретенного сервиса </h1>")
