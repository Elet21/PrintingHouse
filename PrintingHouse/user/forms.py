from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'box-shadow: rgb(116,224,57,)'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']






        
