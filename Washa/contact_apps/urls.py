from django.urls import path 
from .import views
 
urlpatterns = [
    path('contactUs',views.contact,name='contact'),
    
    
]
