from django.contrib import admin
from .models import Tour_Guid,Booking
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ['user_name','name','message_sent','children', 'adult','check_in','email']
    list_display_links = ['user_name','name'] 
    search_fields = ['user_name','id',]
    list_filter = ['user_name',]
    list_editable = ['message_sent','children','adult']


admin.site.register(Booking,BookingAdmin)

class TourGuidAdmin(admin.ModelAdmin):
    list_display = ['t_name','available']
    list_editable = ['available']
    
admin.site.register(Tour_Guid,TourGuidAdmin)