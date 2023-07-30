from django.contrib import admin
from django.urls import path, include, re_path
from .views import *
from keys import views

urlpatterns = [
    path('enter/', enter, name="enter"),
    path('home/',home, name='home'),
    # re_path(r"^activation/(?P<id>[\d-]+)$", home,name='home'),
    path('activate/', activate, name="activate"),
    path('feedback/', feedback, name="feedback"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('package_activation/', package_activation, name="package_activation"),


]