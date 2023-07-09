from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
def enter(request):
    return render(request, "enter.html")

def activate (request):
    return render(request, "activate.html")

def feedback (request):
    return render(request, "feedback.html")

def package_activation (request):
    return render(request, "package_activation.html")



# class LoginUser(LoginRequiredMixin, LoginView):
#     form_class = AuthenticationForm
#     template_name = 'keys/enter.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Авторизация")
#         return dict(list(context.items())+list(c_def.items()))
#
#     def get_user_context(self, title):
#         pass
