from django.contrib import admin
from .models import Booking
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'children', 'adult','check_in','check_out']
    list_display_links = ['name'] 
    search_fields = ['name' , 'children','adult']
    list_filter = ['name']


admin.site.register(Booking,BookingAdmin)