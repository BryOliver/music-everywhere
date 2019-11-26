from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

class RegisterForm(UserCreationForm):
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.is_staff = True
        if commit: 
            user.save()
            my_group = Group.objects.get(name='me-user')
            my_group.user_set.add(user)
        return user 
