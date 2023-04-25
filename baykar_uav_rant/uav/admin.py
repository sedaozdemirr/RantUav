from django.contrib import admin
from .models import Uav,Customer,Reservation
# Register your models here.
class UavSave(admin.ModelAdmin):
    list_display = ('img','brand','model','weight','category', 'airtime','price')
class CustomerSave(admin.ModelAdmin):
    list_display = ('name','email')
class ReservationSave(admin.ModelAdmin):
    list_display = ('customer','uav','issue_date','return_date')

admin.site.register(Uav, UavSave)
admin.site.register(Customer, CustomerSave)
admin.site.register(Reservation, ReservationSave)