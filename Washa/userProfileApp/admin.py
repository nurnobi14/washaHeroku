from django.contrib import admin
from django.forms.models import ModelFormMetaclass

#import your classes.
from .models import Header_footerData
from .models import bannarLayout
from .models import FormLayout
from .models import allRegister 
 
 

# Register your models here.
admin.site.register(Header_footerData)
admin.site.register(bannarLayout)
admin.site.register(FormLayout)
admin.site.register(allRegister)
 
