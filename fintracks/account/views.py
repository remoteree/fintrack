from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
@login_required(login_url='user-login')
def user_dashboard(request):
    return render(request, 'account/user-dashboard.html')

def user_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
    context = {'form':form}
    messages.success(request, "Registered successfully")
    return render(request, 'account/register.html', context)

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect('user-dashboard')
    context = {'form':form}
    return render(request, 'account/login.html', context)

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('index')

