from django.contrib import admin

#import your classes.
from .models import Header_footerData
from .models import shop_banner
from .models import shop_controls
from .models import shopPrduct
from .models import Ordershoped
 

# Register your models here.
admin.site.register(Header_footerData)
admin.site.register(shop_banner)
admin.site.register(shop_controls)
admin.site.register(shopPrduct)
admin.site.register(Ordershoped)
