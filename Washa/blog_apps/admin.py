from django.contrib import admin

#import your classes.
from .models import Header_footerData
from .models import blog_banner
from .models import blog_content
 
 

# Register your models here.
admin.site.register(Header_footerData)
admin.site.register(blog_banner)
admin.site.register(blog_content)
 
 
