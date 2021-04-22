from django.contrib import admin
from django.urls import path,include 
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render
#================
from django.contrib import admin

#admin.site.site_header = 'My project'                    # default: "Django Administration"
admin.site.index_title = 'E-buy'                 # default: "Site administration"
admin.site.site_title = 'dhashboard'

#================
#from django.contrib.auth import views as auth_views
def administrator(request):
    return render(request, 'admin_index.html')
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrator/',  administrator), #custom admin panel
    path('',include('visitor.urls')),
    path('',include('about_apps.urls')),
    path('',include('shop_apps.urls')),
    path('',include('blog_apps.urls')),
    path('',include('contact_apps.urls')),
    path('',include('userProfileApp.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = 'visitor.views.error_404_view'



