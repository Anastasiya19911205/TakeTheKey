from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('key/', key, name="key"),
    path('activate/', activate, name="activate"),
    path('feedback/', feedback, name="feedback"),



]