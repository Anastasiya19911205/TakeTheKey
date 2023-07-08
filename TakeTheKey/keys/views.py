from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
def key (request):
    return render(request, "key.html")

def activate (request):
    return render(request, "activate.html")

def feedback (request):
    return render(request, "feedback.html")



class LoginUser(LoginRequiredMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'keys/key.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items())+list(c_def.items()))

    def get_user_context(self, title):
        pass
