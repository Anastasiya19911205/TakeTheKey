from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('key/', LoginUser.as_view(), name="key"),
    path('activate/', activate, name="activate"),
    path('feedback/', feedback, name="feedback"),



]