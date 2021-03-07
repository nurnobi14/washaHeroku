from django.contrib import admin

# Register your models here.
#import your classes.
from .models import Header_footerData
from .models import contact_banner
from .models import contact_address
from .models import contact_messagesHeade_button
from .models import msgBox
 
 
# Register your models here.
admin.site.register(Header_footerData)
admin.site.register(contact_banner)
admin.site.register(contact_address)
admin.site.register(contact_messagesHeade_button)
admin.site.register(msgBox)
 
