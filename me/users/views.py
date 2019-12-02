from django.shortcuts import render, redirect
from core.views import index
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm

'''Controlador responsável por respondar a uma requisição de registro de um usuário no sistema'''
def register(request):
    context = {}
    '''O usuário é cadastrado a partir de um formulário e por questão de segurança verificamos se o método é do tipo POST, 
    método seguro de envio de informações.'''
    if request.method == 'POST':
        '''Apos a validação do método, cria-se uma variável que armazena as informações contidas nos campos do formulário'''
        form = RegisterForm(request.POST)
        '''Verifica-se se o formulário encontra-se válido, devido as restrições de cada campo, como a senha e a confirmação de senha estarem iguais'''
        if form.is_valid():
            context['is_valid'] = True
            '''Depois de validado tentamos salvá-lo no sistema, caso de certo chamos a função index que esta definida no arquivo core.views.
                Caso não consiga-se registralo no sistema recarregamos a página'''
            try:
                form.save()
                return HttpResponseRedirect(reverse('index'))
            except:
                return HttpResponseRedirect(reverse('register'))
    else:
        form = RegisterForm()
    
    context = {
        'form': form,
    }
    return render(request, 'cadastro.html', context)


def logout_view(request):
    '''Método que logout do sistema, que utilizado o logout padrão do django e rediceriona o usuário para a view de Login'''
    logout(request)
    return HttpResponseRedirect(reverse('login'))
