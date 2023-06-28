from django import forms
from . models import Booking

class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields='__all__'
        widgets = {
            'booking_date':DateInput()
        }
        labels ={
            'p_name':'Enter Name',
            'p_email':'Email',
            'p_phone':'Phone',
            'doc_name':'Doctore Name',
            'booking_date':'Booking Date'
        }