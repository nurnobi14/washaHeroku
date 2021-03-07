from django.shortcuts import render
from .models import Header_footerData
from .models import contact_banner
from .models import contact_address
from .models import contact_messagesHeade_button
from .models import msgBox

# Create your views here.
def contact(request):
    data = Header_footerData.objects.all()
    bannerdata = contact_banner.objects.all()
    addressData = contact_address.objects.all()
    contactHeads = contact_messagesHeade_button.objects.all()
     
    
    context = {
        'datas': data,
        'banner': bannerdata,
        'address': addressData,
        'messegeHead': contactHeads, 
    }
    
    if request.method == "POST":
        fName = request.POST.get('fname')
        lName = request.POST.get('lname')
        number = request.POST.get('phone')
        loc = request.POST.get('locations')
        cmnts = request.POST.get('cmnt')

        msgData = msgBox(
            f_name =fName,
            L_name = lName,
            phone = number,
            location = loc,
            comment = cmnts
        )
        msgData.save()
    
    return render(request,'contact.html',context)