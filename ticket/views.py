from django.shortcuts import render,redirect
from .forms import BookingForm,Booking
from .models import Tour_Guid
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mass_mail
# Create your views here.

def takeBooking(request):

    addbooking = BookingForm(request.POST or None)
    if addbooking.is_valid():
        addbooking.save()
        tour_site_name = addbooking.cleaned_data['name']
        children = addbooking.cleaned_data['children']
        adult = addbooking.cleaned_data['adult']
        check_in = addbooking.cleaned_data['check_in']
        check_out = addbooking.cleaned_data['check_out']
        email = addbooking.cleaned_data['email']
        messages.success(request, f'you have booked for { tour_site_name } an email was sent to the account you provided ')

        # mass mail
        email_from = settings.EMAIL_HOST_USER
        message_from = ('Hello', f'a user have booked for { tour_site_name } with { children } children and { adult} adults sign in to admin panel for for info', email_from, ['aggrey.en@live.com', 'aggrey.en@gmail.com',])
        message_to = ('Placed booked for ' f'{ tour_site_name }',' your request have been made will call u soon we promise to make your stay a joyful one', email_from, [email ,])
        send_mass_mail((message_from, message_to), fail_silently=False)

  

        return redirect('toristSite')
    # addbooking = BookingForm()

    # send message
   
    return render(request, 'bookings/addbooking.html' ,{ 'addbooking' : addbooking})


def toureGuids(request):
        tourguid = Tour_Guid.objects.filter(available=True)
       
        
        context = {
            'tourguids': tourguid,
        }
        return render(request, 'bookings/tourguids.html',context)



