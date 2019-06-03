from django.shortcuts import render,get_object_or_404,redirect
from .models import Hotel,Attraction,Food,TouristSite,HotelInfo,AttractionInfo,FoodInfo,Tourist_Site_Info
from ticket.models import Booking 
from django.conf import settings
from django.core.mail import send_mass_mail
from django.db.models import Q
from  datetime import date 
import datetime
# Create your views here.

def homepage(request):
    check_in_date = Booking.objects.all()
    # currentDT = datetime.datetime.now()
    currentDT = date.today().strftime('%Y-%m-%d')
    
  
    for values in check_in_date:
      
        emails = values.email
        dates = values.check_in
      
        newdate =dates.strftime('%Y-%m-%d')
        
        if currentDT in newdate and values.message_sent==False:
            
            username = values.user_name
            user_id = values.id
            place_name = values.name
            user_email = values.email
            print('email is sent to ', user_email)
           
            # print('the name is ', username, 'and id is' , user_id, 'the email is ', user_email)
            # mass mail
            email_from = settings.EMAIL_HOST_USER
            message_from = ('Hello', f' a user with name { username } and id { user_id } is to visit { place_name } today, you can sign in to admin for more info search user by username or id thank you', email_from, ['aggrey.en@live.com',])
            message_to = ('Hello ' f'{ username }',f' your appointment to visit { place_name } is today { currentDT } thank you  ', email_from, [user_email ,])
            # send_mass_mail((message_from, message_to), fail_silently=False)
    
    return render(request,'toresterngh/home.html')

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



def search_hotels(request):
    # queryset_list = Product.objects.filter(available=True)
    queryset_list = HotelInfo.objects.order_by('-date')

    query = request.GET.get('keyword')
    if query:
        queryset_list = queryset_list.filter(Q(name__icontains = query))
    size = len(queryset_list)

    context = {
        'search_result':queryset_list,
        'resultSize': size,
    }

    return render(request,'toresterngh/list hotels.html',context)
