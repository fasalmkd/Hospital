from django.contrib import admin
from . models import Department, Doctors, Booking
admin.site.register(Department)
admin.site.register(Doctors)
class BookingAdmin(admin.ModelAdmin):
    list_display=['p_name','p_phone','doc_name','booking_date']
admin.site.register(Booking,BookingAdmin)
