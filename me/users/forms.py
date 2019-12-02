from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
'''Esse arquivo tem a finalidade de modificar o método de salvar padrão de um novo usuário do Django
    Criamos nosso próprio formulário e o fazemos herdar do formulário padrão do Django (UserCreationForm)
    Assim ele pega todos os campos padrão e apenas precisamos modificar o método Save'''
class RegisterForm(UserCreationForm):
    def save(self, commit=True):
        '''Esse novo método de salvar utiliza o método Save padrão, mas passando um commit = False. Esse commit é um requisito padrão do metodo save,
            mas ele precisa ser True para que o usuário seja salvo, então o Django faz todo o processo de salvamento, incluindo a criptografia da senha,
            mas não consegue finalizar o processo devido ao commit False, e é retornado para nossa própria função Save'''
        user = super(RegisterForm, self).save(commit=False)
        '''Atribuimos ao usuário a permissão de Staff, o que permite que entre na área de administração'''
        user.is_staff = True
        if commit: 
            '''Atribuimos ao usuário o grupo me-user que da a ele permissão de criar, atualizar, ver e deletar objetos da nossa aplicação Core.
                Depois salvamos o usuário chamando a função save com um commit True'''
            user.save()
            my_group = Group.objects.get(name='me-user')
            my_group.user_set.add(user)
        return user 
