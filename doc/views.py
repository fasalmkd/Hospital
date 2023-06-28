from django.shortcuts import render
from django.http import HttpResponse
from . forms import BookingForm

from . models import Department,Doctors,Booking
def index(request):
   return render(request,"index.html")
def department(request):
   department=Department.objects.all()
   return render(request,"department.html",{'department':department})
def doctor(request):
   doctor=Doctors.objects.all()
   return render(request,"doctor.html",{'doctor':doctor })
def booking(request):
   booking=BookingForm()
   if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Thank You</h1>')
   return render(request,"booking.html",{'form':booking})
   

# Create your views here.
