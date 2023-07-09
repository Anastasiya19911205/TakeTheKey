from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('enter/', enter, name="enter"),
    path('activate/', activate, name="activate"),
    path('feedback/', feedback, name="feedback"),
    path('package_activation/', package_activation, name="package_activation"),


]