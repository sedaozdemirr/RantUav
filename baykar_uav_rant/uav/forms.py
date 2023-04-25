from django import forms

from .models import Uav,Customer,Reservation

class UavSaveForm(forms.ModelForm):

    class Meta:
        model = Uav
        fields = ('img','brand','model','weight','category', 'airtime','price')

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name','email')
class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('customer','uav','issue_date','return_date')