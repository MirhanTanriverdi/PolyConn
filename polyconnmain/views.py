from django.shortcuts import render
from .models import District, User, Reservation, Event, Cafe
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Polyconn - Not yet but in the future we will be all around ;) ")

def list_district(request):
    districts = District.objects.all()
    return render(request, 'main.html', {'districts': districts})

def list_user(request):
    users = User.objects.all()
    return render(request, 'user.html', {'users': users})

def list_cafe(request):
    cafes = Cafe.objects.all()
    return render(request, 'cafes.html', {'cafes': cafes})

def list_reservation(request):
    reservations = Reservation.objects.all()
    return render(request, 'reserve.html', {'reservations': reservations})