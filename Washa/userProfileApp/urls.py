from django.urls import path 
from .import views
 
urlpatterns = [
     
    path('userAccount_login',views.authlogin,name='login'),
    path('userAccount_SignUp',views.userRegister,name='regiteer'),
    path('FrogotPassword',views.userForgot,name='forgotpass'),
    path('User+Veryfication',views.userVerify,name='Userveryfi'),
    path('User+=set-Repassword',views.UserRepass,name='repass'),
    path('UserProfile',views.Userprofile,name='profile'), 
    path('UserLogout',views.Userlogout,name='logout'), 
    
    
]