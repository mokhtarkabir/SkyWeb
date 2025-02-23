from django.shortcuts import render

# Create your views here.
def servicesPage(request):
    return render(request, 'services/services.html')