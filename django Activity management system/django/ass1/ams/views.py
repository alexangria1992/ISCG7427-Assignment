from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import User,Role
from django.db import IntegrityError

from . import forms


def home(request):
    
    return render(request,'home.html',{'includeNav':True})



def child_profile(request):
    return render(request,'child-profile.html',{'includeNav':True})


def my_profile(request):
    cf = forms.ChildForm()
    
    
  
    if request.method == 'POST':
        cf = forms.ChildForm(request.POST)
        
        val =request.POST.get('date_of_birth')
        
        print(val)
        if cf.is_valid():
            child = cf.save()
            request.user.myChildren.add(child)
            messages.add_message(request, messages.SUCCESS, "Child Added Successfully")
        else:
            messages.add_message(request, messages.INFO, "Child Add Failed")
        
    myChildren = request.user.myChildren.all()
    
    context= {'includeNav': True, 'myChildren': myChildren,'form':cf}
    
    return render(request, 'my-profile.html',context)


def add_activity(request):
    return render(request,'add-activity.html',{'includeNav':True})





def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO, "please check your username and/or password")
    


    return render(request,'login.html',{'includeNav':False})





def logout_view(request):
    if (request.user.is_authenticated):
        logout(request)
    return redirect('login')

def register_view(request):
    if(request.user.is_authenticated):
        return redirect('home')
    try:
        if (request.method == 'POST'):
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            userType = request.POST.get("userType")
            user = User.objects.create_user(username, email, password)
            if user is not None:
               #messages.add_message(request, level, message, extra_tags='', fail_silently=False)
                user.roles.add(Role.objects.get(id=userType))
                messages.add_message(request, messages.INFO, "your account was created successfully please log in now")
                # A backend authenticated the credentials
                return redirect( 'login')
    except IntegrityError:
        messages.add_message(request, messages.INFO, "That Username is taken please try another username")

    return render(request,'register.html',{'includeNav':False})