from django.db import models
from toresterngh.models import Tourist_Site_Info
# Create your models here.

class Booking(models.Model):
    name = models.ForeignKey(Tourist_Site_Info, on_delete=models.CASCADE,verbose_name = 'toursite', help_text='select the site to book')
    children = models.PositiveSmallIntegerField('number of children',default=0,null=True)
    adult = models.PositiveSmallIntegerField('number of adult',default=0,null=True)
    check_in = models.DateField()
    check_out = models.DateTimeField()
    email = models.EmailField(help_text= 'enter your email that we can reach you with',null=True)
    dateadd = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

