from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('faq',views.faq,name ='faq'),
    path('sites',views.allSites, name='toristSite'),
    path('moreinfo/<int:about_id>/',views.aboutSite,name ='aboutSites'),
    path('hotels',views.hotels, name ='hotels'),
    path('hotel_info/<int:abouthotel_id>/',views.aboutHotel,name = 'abouthotel'),
    path('aboutpage',views.aboutPage,name = 'aboutpage'),
    path('search',views.search_hotels,name = 'search'),
]

