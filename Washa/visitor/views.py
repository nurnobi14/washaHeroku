from django.shortcuts import render
from django.http import HttpResponse
from .models import Header_footerData, feature_header
from .models import slider_part
from .models import shipping_data
from .models import special_part
from .models import feature_header
from .models import feature_product
from .models import newProduct
from .models import LatestProduct
from .models import testimonial
from .models import My_blog
from .models import Ordered_product
from django.db.models import Q


def home(request):
    data = Header_footerData.objects.all()
    slider_data = slider_part.objects.all()
    shipping = shipping_data.objects.all()
    specialData = special_part.objects.all()
    feature_head = feature_header.objects.all()
    feature_body = feature_product.objects.all()
    new_product = newProduct.objects.all()
    latest_product = LatestProduct.objects.all()
    testimonialData = testimonial.objects.all()
    blog_data = My_blog.objects.all()
    #for search:
    search = request.GET.get('query')
    if search:
        feature_body = feature_body.filter(
            Q(product_title__icontains= search)|Q(product_code__icontains = search)
        )
        latest_product = latest_product.filter(
            Q(P_name__icontains = search)
        )
        specialData = specialData.filter(
            Q(product_name__icontains = search)
        ) 
        #lll:
        feature_head = feature_head.filter(
            Q(header__icontains = search)
        )
        new_product = new_product.filter(
            Q(header__icontains = search)
        )
        testimonialData = testimonialData.filter(
            Q(header__icontains = search)
        )
        shipping = shipping.filter(
            Q(header__icontains = search)
        )
        slider_data = slider_data.filter(
            Q(Header__icontains = search)
        )
         
    global context
    context = {
        'datas':data,
        'sliderData':slider_data,
        'shippings' :shipping,
        'special' :specialData,
        'featuer_heads' :feature_head,
        'featuer_goods' :feature_body,
        'launchProduct' : new_product,
        'latest' : latest_product,
        'Testimonial' : testimonialData,
        'Blogs' : blog_data
        
    }
    #order data:
    if request.method == "POST":
        email = request.POST.get('email')
        number = request.POST.get('Mobile')
        p_code = request.POST.get('productCode')
        address = request.POST.get('address')

        orderData = Ordered_product(
            mail =email,
            number = number,
            product_Code = p_code,
            location = address,
        )
        orderData.save()
     
    return render(request,'index.html', context ) 



#def about(request):
    return render(request,'about.html',context)

#def shop(request):
    #return render(request,'product.html',context)

#def blog(request):
    return render(request,'blog.html',context)

#def contact(request):
    return render(request,'contact.html',context)

#def singUp(request):
    return render(request,'registration.html',context)


