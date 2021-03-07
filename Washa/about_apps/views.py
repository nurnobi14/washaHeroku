from django.shortcuts import render
from .models import about_banner
from .models import about_stroy
from .models import about_counter
from .models import about_designer
from .models import Header_footerData

def about(request):
    data = Header_footerData.objects.all()
    bannaer = about_banner.objects.all()
    storyData = about_stroy.objects.all()
    counterData = about_counter.objects.all()
    designerData = about_designer.objects.all()
    
    context = {
        'datas': data,
        'bannerData': bannaer, 
        'story': storyData,
        'counter': counterData,
        'designer': designerData,
        
    }
    return render(request,'about.html',context) 
