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
    
class blog_banner(models.Model):
    header = models.CharField(max_length=50)    
    title1 = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)

class blog_content(models.Model):
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
