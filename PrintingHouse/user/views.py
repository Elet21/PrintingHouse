from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib import auth 
from django.contrib.auth.views import LoginView

from .forms import RegistrationForm, LoginForm


def my_logout(reuqests):
    logout(reuqests)
    return redirect('all_list')



class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'registration/login.html'
# class Login(View):
#     template_name = 'user/login.html'

#     def get(self, request):
#         context = {
#             'form': LoginForm()
#         }
#         return render(request, 'user/login.html', context)

#     def post(self, request):
#         form = LoginForm(request.POST)

#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             auth.login(request, user)
#             # session_key = request.session.session_key


#         else:
#             context = {
#                 'form': form
#             }
#         return render(request, 'user/login.html', context)


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

