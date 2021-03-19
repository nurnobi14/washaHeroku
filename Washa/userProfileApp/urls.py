from django.http import request
from django.shortcuts import redirect
from django.urls import path 
from .import views
from django.http.response import HttpResponseRedirect
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView  
 
urlpatterns = [
     
    path('userAccount_login',views.authlogin,name='login'),
    path('userAccount_SignUp',views.userRegister,name='regiteer'),
    path('UserProfile',views.Userprofile,name='profile'), 
    path('UserLogout',views.Userlogout,name='logout'), 
    
    path('reset/password/',PasswordResetView.as_view(template_name = 'forgot.html'),name='password_reset'),
    path('reset/password/done/',PasswordResetDoneView.as_view(template_name = 'resetDone.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'),name='password_reset_complete'),
    
    
]