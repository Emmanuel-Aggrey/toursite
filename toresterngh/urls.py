from django.urls import path
from . import views
urlpatterns = [
    path('faq',views.faq,name ='faq'),
    path('',views.allSites, name='toristSite'),
    path('moreinfo/<int:about_id>/',views.aboutSite,name ='aboutSites'),
    path('hotels',views.hotels, name ='hotels'),
    path('hotel_info/<int:abouthotel_id>/',views.aboutHotel,name = 'abouthotel'),
    path('aboutpage',views.aboutPage,name = 'aboutpage'),
]

