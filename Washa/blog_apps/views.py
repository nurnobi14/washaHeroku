from django.shortcuts import render
from .models import Header_footerData
from .models import blog_banner
from .models import blog_content

# Create your views here.
def blog(request):
    
    data = Header_footerData.objects.all()
    blogData = blog_banner.objects.all()
    blogContent = blog_content.objects.all()
    context = {
        'datas': data,
        'blogs': blogData,
        'blogsContent': blogContent,
        
    }
    return render(request,'blog.html',context)
