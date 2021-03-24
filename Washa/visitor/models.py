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

class slider_part(models.Model):
    year = models.CharField(max_length=5,blank=False)
    Header = models.CharField( max_length=30,blank=False)
    describe = models.TextField(max_length=500,blank=False)
    left_button = models.CharField(max_length=50,blank=False)
    right_button = models.CharField(max_length=50,blank=False)       
    slider_images = models.ImageField(upload_to='slider_img/',default ="")

 
class shipping_data(models.Model):
    header = models.CharField( max_length=50,blank=False)
    details = models.TextField(max_length=350,blank=False)   
    
    
    def __str__(self):
        return self.header
    

#now start special part:

class special_part(models.Model):
    img = models.ImageField(upload_to="special_images/")
    product_head = models.CharField(max_length=50,blank=False)
    product_name = models.CharField(max_length=250,blank=False)    
    button_name = models.CharField(max_length=50,blank=False)


# now fetured part :

class feature_header(models.Model):
    header = models.CharField(max_length=50,blank=False)
    menu1 = models.CharField(max_length=50,blank=False)
    menu2 = models.CharField(max_length=50,blank=False)
    menu3 = models.CharField(max_length=50,blank=False)
    menu4 = models.CharField(max_length=50,blank=False)
    menu5 = models.CharField(max_length=50,blank=False)
    


class feature_product(models.Model):
    product_img = models.ImageField(upload_to="feature_images/")
    product_title = models.CharField(max_length=50 ,blank=False)        
    product_price = models.CharField(max_length=50,blank=False)
    product_code = models.CharField(max_length=50,blank=False,default="")


#microsoft part now:

class newProduct(models.Model):
    header = models.CharField(max_length=50,blank=False)
    img = models.ImageField(upload_to="launchImages/")
    productName =models.CharField(max_length=50,blank=False)
    details = models.TextField(max_length=250,blank=False)
    launchTitle = models.CharField(max_length=50,blank=False)
    month = models.CharField(max_length=5,blank=False,default ="")
    day  = models.CharField(max_length=5,blank=False,default ="")
    year = models.CharField(max_length=5,blank=False,default ="")
    
# letest product:

class LatestProduct(models.Model):
    header = models.CharField(max_length=50,blank=False)
    img  = models.ImageField(upload_to="latest_img/")
    P_name = models.CharField(max_length=50,blank=False)
    P_price = models.CharField(max_length=10,blank=False)    
    
    def __str__(self) -> str:
        return self.P_name


class testimonial(models.Model):
    header = models.CharField(max_length=50,blank=True)
    personName = models.CharField(max_length=50,blank=False)
    personTitle = models.CharField(max_length=50,blank=False)
    personImg =  models.ImageField(upload_to="testimonial/")
    describe = models.TextField(max_length=220,blank=False)
    signature = models.CharField(max_length=15,blank=False)
    
    def __str__(self) -> str:
        return self.personName

class My_blog(models.Model):
    header = models.CharField(max_length=50,blank=True)
    img = models.ImageField(upload_to="blogImg/")
    date = models.DateTimeField(blank=True)
    author_by = models.CharField(max_length=50,blank=False)
    like = models.CharField(max_length=50,blank=False)
    cmnt = models.CharField(max_length=50,blank=False)
    title = models.CharField(max_length=50,blank=False)
    describe = models.TextField(max_length=250,blank=False)
    button = models.CharField(max_length=50,blank=False)
    
    def __str__(self) -> str:
        return self.title
 
     
     
    
 