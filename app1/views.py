from multiprocessing import AuthenticationError
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def login_handle(request):
    if request.method== 'POST':
        loginusername=request.POST['username']
        loginpassword=request.POST['password']
        user =authenticate(username='loginusername',password='loginpassword')
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully your Logged into Admin-Panel")
            return redirect('home')
        else:
            messages.error(request,"Invalid User Details! Login with proper Credentials")
            return redirect('login')