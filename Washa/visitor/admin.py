from django.contrib import admin

from .models import Header_footerData
from .models import slider_part
from .models import shipping_data
from .models import special_part
from .models import feature_header
from .models import feature_product
from .models import newProduct
from .models import LatestProduct 
from .models import testimonial
from .models import My_blog

admin.site.register(Header_footerData)
admin.site.register(slider_part)
admin.site.register(shipping_data)
admin.site.register(special_part)
admin.site.register(feature_header)
admin.site.register(feature_product)
admin.site.register(newProduct)
admin.site.register(LatestProduct)
admin.site.register(testimonial)
admin.site.register(My_blog)
 
