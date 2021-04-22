from django.conf.urls import url
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import  Header_footerData
from .models import  bannarLayout
from .models import  FormLayout
from .models import  allRegister
#from .models import  profilePhoto
#=============
# For message
from django.contrib import messages
#=============
 

# Create your views here.

def authlogin(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request,username = name,password = password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            print('invalid username or password!')
            messages.error(request,'invalid username or password!')
    
    data = Header_footerData.objects.all()
    banner = bannarLayout.objects.all()
    formdata = FormLayout.objects.all()
    
    
    context = {
        'datas': data,
        'bannerdatas': banner,
        'formsdata': formdata,
    }
       
    return render(request,'login.html',context)           

def userRegister(request):
    if request.method == "POST":
        
        first_name =  request.POST.get('first_name')
        names =  request.POST.get('username')
        mails =  request.POST.get('email')
        pass1 =  request.POST.get('password1')
        pass2 =  request.POST.get('password2')
        #messages.success(request,'registration successfully')
        
        UserData = allRegister(
            first_name = first_name,
            userName = names,
            userMail =  mails,
            userPass =  pass1,
            userConPass = pass2
        )
        UserData.save()
    # register authentications start:
    
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'This Username already exist')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'This Email already exist') 
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name = first_name)
                user.save()  
                messages.success(request,'registration successfully')
                return redirect('login')     
                 
        else:
            messages.error(request,'password & confirm_password not matched')
                
    # register authentications end:
     
    data = Header_footerData.objects.all()
    banner = bannarLayout.objects.all()
    formdata = FormLayout.objects.all()
    
    context = {
        'datas': data,
        'bannerdatas': banner,
        'formsdata': formdata,
         
    }
        
    return render(request,'registration.html',context)

def Userprofile(request):
     
    if request.user.is_authenticated:
        data = Header_footerData.objects.all()
        
    
        context = {
             'datas': data,   
        }
        return render(request, 'profile.html',context)
    else:
        return redirect('login')
    
     

def Userlogout(request):
    logout(request)
    return redirect('login')