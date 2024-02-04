from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def registers(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if register.objects.filter(username=username).exists():
                messages.info(request,"Username Already exist")
                return redirect('register')
            elif register.objects.filter(email=email).exists():
                messages.info(request,"Email Already exist")
                return redirect('register')
            else:
                user=register.objects.create(firstname=firstname,lastname=lastname,username=username,email=email,password=password1)
                user.save()
                messages.info(request,"Registration Successful")
        else:
            messages.info(request,"Password mismatch")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,"register.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid User")
            return redirect('login')
    else:
        return render(request, "login.html")

# def logout(request):
#     auth.logout(request)
#     return redirect('/')