from django.db import models
from django.db.models import base
from django.db.models.fields import DateTimeField
from django.db.models.fields.files import ImageField

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

class shop_banner(models.Model):
    header = models.CharField(max_length=50,blank=True,default='')
    title1 = models.CharField(max_length=50,blank=False,default='')
    title2 = models.CharField(max_length=50,blank=False,default='')
    
class shop_controls(models.Model):
    title1 = models.CharField(max_length=50,blank=True,default='')
    sortedBy = models.CharField(max_length=50,blank=False,default='')
    title2 = models.CharField(max_length=50,blank=True,default='')
    NumberOfshowPruduct = models.CharField(max_length=50,blank=False,default='')
    title3 = models.CharField(max_length=50,blank=True,default='')
    pages = models.CharField(max_length=50,blank=False,default='')
    #lastOfPage_number = models.CharField(max_length=50,blank=True,default='')
    lastOfPage_number = models.IntegerField(default=10,blank=True) 
    
#start show products class :
class shopPrduct(models.Model):
    img = models.ImageField(upload_to="shop_productImgs/")
    p_name = models.CharField(max_length=50,blank=False)
    p_price_usd = models.IntegerField(blank=False)
    product_code = models.CharField(max_length=50,blank=False)
    
    def __str__(self) -> str:
        return self.p_name

class Ordershoped(models.Model):
    mail = models.CharField(max_length=50,blank=False) 
    number = models.CharField(max_length=50,blank=False) 
    product_Code = models.CharField(max_length=50,blank=False) 
    location = models.CharField(max_length=50,blank=False) 
    
    def __str__(self) -> str:
        return self.number
    
         