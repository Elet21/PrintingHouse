from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib import auth 
from django.contrib.auth.views import LoginView

from .forms import RegistrationForm, LoginForm
from cart.models import Cart


def my_logout(reuqests):
    logout(reuqests)
    return redirect('all_list')



class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'registration/login.html'


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': RegistrationForm()
        }
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
        else:
            context = {
                'form': form
            }
        return render(request, 'registration/register.html', context)


def cart(requests):
    return render(requests, 'user_cart.html')