from django.urls import path 
from .import views
 
urlpatterns = [
     
    path('aboutUs',views.about,name='about'),
    
    
]