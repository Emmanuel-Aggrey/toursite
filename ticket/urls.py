from django.urls import path
from . import views
urlpatterns = [
    path('',views.takeBooking,name ='booking'),

]
   