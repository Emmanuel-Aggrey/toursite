from django.urls import path
from .import views
urlpatterns = [
    path('',views.takeBooking,name ='booking'),
    path('tourguids',views.toureGuids,name ='persons'),

]
   