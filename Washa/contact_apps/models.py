from django.db import models

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
    

class contact_banner(models.Model):
    header = models.CharField(max_length=50,blank=False)
    title1 = models.CharField(max_length=50,blank=False)
    title2 = models.CharField(max_length=50,blank=False)

class contact_address(models.Model):
    header = models.CharField(max_length=50,blank=False)  
    details = models.TextField(max_length=250,blank=False)  
    location = models.CharField(max_length=250,blank=False)
    mobile = models.CharField(max_length=50,blank=False)
    mobile2 = models.CharField(max_length=50,blank=False)
    mail = models.CharField(max_length=50,blank=False)
    website = models.CharField(max_length=50,blank=False)
    website2 = models.CharField(max_length=50,blank=False)
    
class contact_messagesHeade_button(models.Model):
        header = models.CharField(max_length=50,blank=False)  
        button_Name = models.CharField(max_length=50,blank=False)  

class msgBox(models.Model):
    f_name = models.CharField(max_length=50)  
    L_name = models.CharField(max_length=50)  
    phone = models.CharField(max_length=50)
    location = models.CharField(max_length=150)          
    comment = models.TextField(max_length=300)
    
    def __str__(self) -> str:
        return self.phone