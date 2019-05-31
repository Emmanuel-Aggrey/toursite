from django.contrib import admin
from .models import Hotel,Attraction,Food,TouristSite,HotelInfo,AttractionInfo,FoodInfo,Tourist_Site_Info
# Register your models here.

   
# ABSTRACT MODELS
class DisplayHotelInfo(admin.ModelAdmin):
    list_display = ['name','phone']
    list_filter = ['name','phone']
    search_fields = ['name','phone']


class DisplayAttractionInfo(admin.ModelAdmin):
    list_display = ['name','phone']
    list_filter = ['name','phone']
    search_fields = ['name','phone']


class DisplayFooodInfo(admin.ModelAdmin):
    list_display = ['name','phone']
    list_filter = ['name','phone']
    search_fields = ['name','phone']

class DisplayTourist_Site_Info(admin.ModelAdmin):
    list_display = ['name','phone']
    list_filter = ['name','phone']
    search_fields = ['name','phone']

# REGISTERING CATEGORIES MODEL
admin.site.register(Hotel)
admin.site.register(Attraction)
admin.site.register(Food)
admin.site.register(TouristSite)


# INFO MODELS
admin.site.register(HotelInfo,DisplayHotelInfo)
admin.site.register(AttractionInfo,DisplayAttractionInfo)
admin.site.register(FoodInfo,DisplayFooodInfo)
admin.site.register(Tourist_Site_Info,DisplayTourist_Site_Info)

