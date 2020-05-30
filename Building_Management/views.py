from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from .forms import CreateUserForm
from django.contrib import messages


def index(request):
    # if request.user.is_authenticated:
    #     return redirect('index')

    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is Incorrect')

    context = {}
    return render(request,'index.html',context)


def logoutUser(request):
    return redirect('index')

@login_required(login_url='index')
def home(request):
    return render(request,'home.html')

def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('index')


    context = {'form':form}
    return render(request,'signup.html',context)

@login_required(login_url='index')
def businessMngmt(request):
    return render(request,'businessMngmt.html')

def monthlyExpense(request):
    return render(request,'monthlyExpense.html')