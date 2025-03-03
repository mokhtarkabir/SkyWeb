from django.shortcuts import render
from .models import Service
# Create your views here.
def servicesPage(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})


    