from django.shortcuts import render, redirect
from .models import Grocery
from .forms import ProductForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

def regesterpage(request):
    context = {}
    return render(request, 'Insta_grocery/regester.html')

def loginpage(request):
    context = {}
    return render(request, 'Insta_grocery/login.html')


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


def delete_data(request, id):
    if request.method == 'POST':
        pi = Grocery.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    else:
        pi = Grocery.objects.get(pk=id)
    return render(request, 'Insta_grocery/delete.html', {'pi': pi})

