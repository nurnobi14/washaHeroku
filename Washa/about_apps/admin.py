from django.contrib import admin

#import your classes.
from .models import Header_footerData
from .models import about_banner
from .models import about_stroy
from .models import about_counter
from .models import about_designer

# Register your models here.
admin.site.register(Header_footerData)
admin.site.register(about_banner)
admin.site.register(about_stroy)
admin.site.register(about_counter)
admin.site.register(about_designer)