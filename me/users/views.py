from django.shortcuts import render, redirect
from core.views import index
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'cadastro.html', context)
