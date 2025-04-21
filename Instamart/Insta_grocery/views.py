from django.shortcuts import render, redirect
from .models import Grocery
from .forms import ProductForm, CreateUserForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm(request.POST)
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user +'Account created successfully!')
                return redirect('login')  
        else:
            form = CreateUserForm()
        return render(request, 'Insta_grocery/register.html', {'form': form})


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user= authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR Password is incorrect')
        context = {}
        return render(request, 'Insta_grocery/login.html')

def logout_user(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm()
    else:
        form = ProductForm()
    groceries = Grocery.objects.all()
    form = ProductForm()
    return render(request, 'Insta_grocery/home.html', {'groceries': groceries, 'form': form})

@login_required(login_url='login')
def update_data(request, id):
    if request.method == 'POST':
        pi = Grocery.objects.get(pk=id)
        form = ProductForm(request.POST, request.FILES, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        pi = Grocery.objects.get(pk=id)
        form = ProductForm(instance=pi)
    return render(request, 'Insta_grocery/update.html', {'form': form})

@login_required(login_url='login')
def delete_data(request, id):
    if request.method == 'POST':
        pi = Grocery.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    else:
        pi = Grocery.objects.get(pk=id)
    return render(request, 'Insta_grocery/delete.html', {'pi': pi})


