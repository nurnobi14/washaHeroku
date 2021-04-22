from django.shortcuts import render
from .models import Header_footerData
from .models import shop_banner
from .models import shop_controls
from .models import shopPrduct
from .models import Ordershoped

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

#for shopApps Order:
def shop_Order(request):
    if request.method == "POST":
        email = request.POST.get('email')
        number = request.POST.get('Mobile')
        p_code = request.POST.get('productCode')
        address = request.POST.get('address')

        orderDatas = Ordershoped(
            mail =email,
            number = number,
            product_Code = p_code,
            location = address,
        )
        orderDatas.save()
    return render(request,'product.html')    