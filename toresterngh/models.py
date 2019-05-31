from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=100,unique=True)
    date= models.DateTimeField(auto_now_add=True,blank=False,null=True)
  
    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']  


class Hotel(Category):
    pass

class Attraction(Category):     
    pass   


class Food(Category):   
     class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Food'
    
 
class TouristSite(Category):
    pass    

# ADDITIONAL INFO MODEL TO CATEGORY
class MoreInfo(models.Model):
    image = models.ImageField(upload_to='info_images')
    detail= models.TextField()
    phone = models.CharField(blank=True,null=True,help_text='optional',max_length=100) 
    mymap = models.CharField(max_length=100,blank=True,null=True,help_text='dont mind will work on it later')
    date= models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField(upload_to = 'hotel_img/%Y/%m/%d',blank=True,null=True)
    image2 = models.ImageField(upload_to = 'hotel_img/%Y/%m/%d',blank=True,null=True)
    image3 = models.ImageField(upload_to = 'hotel_img/%Y/%m/%d',blank=True,null=True)
  

    def __str__(self):
        return str(self.name)

    class Meta:
        abstract = True



class HotelInfo(MoreInfo):
    name = models.OneToOneField(Hotel,on_delete=models.CASCADE,help_text='select hotel ')
 

    class Meta:
      
        verbose_name = 'About Hotel'
        verbose_name_plural = 'About Hotel'

    def get_absolute_url(self):
        return reverse('abouthotel', args=[self.id])




class AttractionInfo(MoreInfo):
    name = models.OneToOneField(Hotel,on_delete=models.CASCADE,help_text='select hotel ')
 

    class Meta:
      
        verbose_name = 'About Attraction'
        verbose_name_plural = 'About Attraction'

class FoodInfo(MoreInfo):
    name = models.OneToOneField(Hotel,on_delete=models.CASCADE,help_text='select hotel ')

    class Meta:
     
        verbose_name = 'About Food'
        verbose_name_plural = 'About Food'



class Tourist_Site_Info(MoreInfo):
    name = models.OneToOneField(TouristSite,on_delete=models.CASCADE,help_text='select hotel ')
    nearesthotel = models.ManyToManyField(Hotel)

    class Meta:
     
        verbose_name = 'About Tourist Site'
        verbose_name_plural = 'About Tourist Site'


