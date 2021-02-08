from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.forms import CreateUserForm


# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html', {})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'GET':
            return render(request, 'login.html', {})
        else:
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'GET':
        user_form = CreateUserForm()
        return render(request, 'register.html', {'form':user_form})
    else:
        user_form = CreateUserForm(request.POST)
        
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'form':user_form})


