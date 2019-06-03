from django import forms
from . models import Booking


class BookingForm(forms.ModelForm):


    class Meta:
        model = Booking
        fields = [
            'user_name',
            'name',
            'children',
            'adult',
            'check_in',
            'check_out',
            'email',
            'request_guiid',
        ]
        widgets = {
        # 'check_out': forms.DateField(format("%b %d %Y")),
        'check_in': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'check_out': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
       
    }
    
   


     
      