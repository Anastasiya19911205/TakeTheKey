from time import sleep
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import logout


from .forms import LoginUserForm, IviForm
from .utils import *
from .models import *



def enter(request):
    return render(request, "enter.html")

def home(request):
    return render(request, "home.html")
def activate (request):
    return render(request, "activate.html")

def feedback (request):
    return render(request, "feedback.html")

# def login (request):
#     return render(request, "login.html")

def package_activation(request):
    return render(request, "package_activation.html")


# class Register(DataMixin, CreateView):
#     form_class = RegisterUserForm
#     template_name = 'keys/enter.html'
#     success_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Регистрация")
#         return dict(list(context.items())+list(c_def.items()))



class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items())+list(c_def.items()))

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('feedback')


def logout_user(request):
    logout(request)
    return redirect('login')

def feedback(request):
    codes = Ivi.objects.all()
    print (request.method)
    context = {}
    if request.method == 'POST':
        form = IviForm(request.POST)
        context["form"] = form
        if form.is_valid():
            # form_codes.save()
            code_ivi= request.POST['code_ivi']
            code=Ivi.objects.get(code_ivi=code_ivi)
            print(code.name_ivi, code.license_ivi)
            # cache.clear()
            return redirect("home")



    else:
        form = IviForm()
        context["form"] = form

    # context = {
    #     "form": form,
    #     "codes":codes
    # }
    return render(request, "feedback.html", context=context)




# def package(request):
#     codes = Ivi.objects.all()
#     if request.method == "POST":
#         form_code_ivi = IviForm(request.POST)
#         if form_code_ivi.is_valid():
#             form_code_ivi.save()
#             return HttpResponseRedirect('/')
#
#     else:
#         form_code_ivi = IviForm()
#
#
#
#     # grap all TodoItems from database:
#
#
#     # grap all TodoLists (titles) from database:
#     # code = TodoList.objects.all()
#
#     return render(request, 'package_activation.html',
#                   {
#                       'form_code_ivi': form_code_ivi,
#                       'codes':codes
#                   })
# def index(request):
#     codes = Ivi.objects.all()
#     return render(request, "feedback.html", {"codes": codes})

# получение данных из бд
# def index(request):
#     ivi = Ivi.objects.all()
#     return render(request, "feedback.html", {'ivi': ivi})






