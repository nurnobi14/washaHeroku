from django.db import models
from django.db.models import base
from django.db.models.fields import DateTimeField
from django.db.models.fields.files import ImageField

#my classes:
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

class about_banner(models.Model):
    header = models.CharField(max_length=50,blank=False)
    title_1= models.CharField(max_length=50,blank=False)
    title_2= models.CharField(max_length=50,blank=False)
    
class about_stroy(models.base.Model):
    img = models.ImageField(upload_to="storyImage/")
    story = models.TextField(max_length=1000,blank=False)
    
class about_counter(models.Model):
    count_number = models.CharField(max_length=9,blank=False)
    quantity_name = models.CharField(max_length=50,blank=False)
    
    def __str__(self) -> str:
        return self.quantity_name
    
class about_designer(models.Model):
    header = models.CharField(max_length=50,blank=True)
    img = models.ImageField(upload_to="designerImage/") 
    name = models.CharField(max_length=50,blank=False)
    designation = models.CharField(max_length=50,blank=False)     
    
    def __str__(self) -> str:
        return self.name 
       