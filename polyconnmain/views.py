from django.shortcuts import render
from .models import District
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse(District)

def list_districts(request):
    districts = District.objects.all()
    return render(request, 'main.html', {'districts': districts})
