from django.db import models
from toresterngh.models import Tourist_Site_Info
# Create your models here.


class Tour_Guid(models.Model):
    t_name = models.CharField('name', max_length=200,default='Aggrey')
    about = models.TextField()
    image = models.ImageField(upload_to='tourguid_img/%Y/%m/%d',blank=True,null=True)
    available = models.BooleanField(default=False)

    class Meta:
        
        verbose_name = 'Tour Guid'
        verbose_name_plural = 'Tour Guids'

    def __str__(self):
        return self.t_name


class Booking(models.Model):
    user_name = models.CharField('name',max_length=200,null=True)
    name = models.ForeignKey(Tourist_Site_Info, on_delete=models.DO_NOTHING,verbose_name = 'toursite', help_text='select the tour site to book')
    children = models.PositiveSmallIntegerField('number of children',default=0,null=True)
    adult = models.PositiveSmallIntegerField('number of adult',default=0,null=True)
    check_in = models.DateField()
    check_out = models.DateTimeField()
    request_guiid = models.OneToOneField(Tour_Guid,on_delete=models.DO_NOTHING,null=True,blank=True,help_text='optional select a tour guid')
    message_sent = models.BooleanField(default=False)
    email = models.EmailField(help_text= 'enter your email that we can reach you with',null=True)
    dateadd = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-dateadd']
    def __str__(self):
        return str(self.name)

