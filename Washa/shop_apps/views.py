from django.shortcuts import render
from .models import Header_footerData
from .models import shop_banner
from .models import shop_controls
from .models import shopPrduct

# Create your views here.
def shop(request):
    data = Header_footerData.objects.all()
    shopData = shop_banner.objects.all()
    controlsData = shop_controls.objects.all()
    shop_product = shopPrduct.objects.all()
    
    context = {
        'datas': data,
        'shops': shopData,
        'controls': controlsData,
        'shopData': shop_product
        
    }
    return render(request,'product.html',context)