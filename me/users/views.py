from django.shortcuts import render, redirect
from core.views import index
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = RegisterForm()
    
    context = {
        'form': form,
    }
    return render(request, 'cadastro.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
