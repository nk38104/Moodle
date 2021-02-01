from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.forms import CreateUserForm
from .forms import UserAuthenticationForm


# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html', {})


def login_user(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'GET':
            return render(request, 'login.html', {})
        elif request.method == 'POST':
            username = request.POST.get('email')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'login.html', {'user':user})
        else:
            return HttpResonseNotAllowed()
    # user = request.user
    
    # if user.is_authenticated:
    #     return redirect('index')

    # if request.POST:
    #     form = UserAuthenticationForm(request.POST)
    #     if form.is_valid():
    #         email = request.POST['email']
    #         password = request.POST['password']
            
    #         user = authenticate(email=email, password=password)
            
    #         if user:
    #             login(request, user)
    #             return redirect('index')
    #         else:
    #             return render(request, 'login.html', {'user':user})
    #     else:
    #         return render(request, 'login.html', {})
    # else:
    #     return render(request, 'login.html', {})


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'GET':
            user_form = CreateUserForm()
            return render(request, 'register.html', {'form':user_form})
        elif request.method == 'POST':
            user_form = CreateUserForm(request.POST)

            if user_form.is_valid():
                user_form.save()
                return redirect('login')
            else:
                return render(request, 'register.html', {'form':user_form})
        else:
            return HttpResonseNotAllowed()


