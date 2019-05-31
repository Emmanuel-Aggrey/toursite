from django.shortcuts import render,get_object_or_404,redirect
from .models import Hotel,Attraction,Food,TouristSite,HotelInfo,AttractionInfo,FoodInfo,Tourist_Site_Info

# Create your views here.
def faq(request):
    return render(request, 'partials/faq.html')
# TOUR SITES
def allSites(request):
    all_ToristSite = Tourist_Site_Info.objects.all()
  
    context = {
        'all_ToristSite':all_ToristSite,
       
    }
    return render(request,'toresterngh/list_sites.html',context)



def aboutSite(request,about_id):

    aboutSite = get_object_or_404(Tourist_Site_Info, id = about_id)
    near_hotels = aboutSite.nearesthotel.all()

    context ={
        'abouthotel': aboutSite,
        'near_hotels':near_hotels,
    }

    return render(request,'toresterngh/about_site.html',context)

    # HOTELS
def hotels(request):
    all_hotels = HotelInfo.objects.all()
  
    context = {
    'all_ToristSite':all_hotels,
       
    }
    return render(request,'toresterngh/list hotels.html',context)

def aboutHotel(request,abouthotel_id):

    abouthotel = get_object_or_404(HotelInfo, id = abouthotel_id)
    # near_hotels = abouthotel.nearesthotel.all()

    context ={
        'abouthotel': abouthotel,
        # 'near_hotels':near_hotels,
    }

    return render(request,'toresterngh/about_hotel.html',context)


def aboutPage(request):
    return render(request,'toresterngh/aboutpage.html')

