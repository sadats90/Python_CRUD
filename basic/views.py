# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm,EmpForm
from django.contrib.auth.models import User
from  .models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()
	    return redirect("/")
    else:
	    form = RegisterForm()

    return render(response, "register/register.html", {"form":form})



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'register/login.html', context)   


def logoutUser(request):
    logout(request)
    return redirect('login')


def cc(request):
    
    if request.user.is_authenticated:
        profile = Profile.objects.all()

        if request.method == "POST":
            form  = EmpForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
            return redirect("/")
        else:
            form = EmpForm()
            return render(request,"register/page.html",{"form":form,"profile":profile})   
    else:
        return redirect('login')


def updateOrder(request, pk):
    usr = Profile.objects.get(id=pk)
    form = EmpForm(instance=usr)

    if request.method == 'POST':
        form = EmpForm(request.POST,request.FILES, instance=usr)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request,'register/update.html',{"form":form})





def deleteOrder(request, pk):
    usr = Profile.objects.get(id=pk)
    if request.method == "POST":
        usr.delete()
        return redirect('/')

    
    return HttpResponse("deleted successfully")   



  
