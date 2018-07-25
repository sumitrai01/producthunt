from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method=='POST':
        #user wants to post something to server
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'signup.html',{'error':'username has been taken already'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'signup.html',{'error':'password must match'})

    else:
        #user wants to get something from server
        return render(request,'signup.html')
def login(request):
    if request.method == 'POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'login credentials are invalid'})
    else:
        return render(request,'login.html')
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
