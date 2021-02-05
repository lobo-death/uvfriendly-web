from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

template_name = 'accounts'

def forgot_password(request):
    return render(request, 'forgot-password.html')

def login(request):
    return render(request, 'login.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'