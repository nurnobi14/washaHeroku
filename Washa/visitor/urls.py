from django.urls import path 
from .import views
 
urlpatterns = [
    path('',views.home,name='home'),
    #path('aboutUs',views.about,name='about'),
    
    #path('shoping',views.shop,name='shop'),
    #path('blogs',views.blog,name='blog'),
    #path('contactUs',views.contact,name='contact'),
    #path('singUp',views.singUp,name='singup'),
    
    
]
