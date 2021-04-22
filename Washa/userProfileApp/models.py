from django.db import models
from django.db.models import fields
from django.db.models.fields.files import ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



from django import forms

# Create your models here.
class Header_footerData(models.Model):
    number_title = models.CharField(max_length=50,blank=False)
    number = models.CharField(max_length=15,blank=False)
    logo = models.ImageField(upload_to='logoimage/')
    # start for footer part:
    footerLogo_describ = models.TextField(max_length=500,blank=False,default='')
    footerLogo_describ_2 = models.TextField(max_length=500,blank=False,default='')
    footerContact_header = models.CharField(max_length=50,blank=False,default='')
    footerContact_location= models.CharField(max_length=200,blank=False,default='')
    footerContact_telePhone = models.CharField(max_length=50,blank=False,default='')
    footerContact_mail = models.CharField(max_length=50,blank=False,default='')
    footerContact_webSite = models.CharField(max_length=70,blank=False,default='')
    copyRight = models.CharField(max_length=50,blank=False,default='')
    copyRightBy = models.CharField(max_length=50,blank=False,default='')


class bannarLayout(models.Model):
    header = models.CharField(max_length=50,blank=False)
    title1 = models.CharField(max_length=50,blank=False)
    title2 = models.CharField(max_length=50,blank=False)
    
class FormLayout(models.Model):
    loginHeader = models.CharField(max_length=50,blank=False)
    logintitle = models.CharField(max_length=50,blank=False)
    registerHeader = models.CharField(max_length=50,blank=False)
    hint = models.CharField(max_length=50,blank=False)
    RegisterTitle = models.CharField(max_length=50,blank=False)

class allRegister(models.Model):
    first_name = models.CharField(max_length=50,blank=True)
    userName = models.CharField(max_length=50,blank=True)
    userMail = models.CharField(max_length=50,blank=True)
    userPass = models.CharField(max_length=50,blank=True)
    userConPass = models.CharField(max_length=50,blank=True)
    
    def __str__(self) -> str:
        return self.userMail

     
 
     
     
        