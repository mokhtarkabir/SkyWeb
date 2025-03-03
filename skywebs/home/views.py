from django.shortcuts import render

from services.models import Service
from about.models import AboutPage, TeamMember
# Create your views here.

def homePage(request):
    services = Service.objects.all()[:3]
    aboutpage = AboutPage.objects.all()[:1]
    teamMember = TeamMember.objects.all()
    context={
        'services': services,
        'aboutpage':aboutpage,
        'teamMember':teamMember
    }
    return render(request, 'home/home.html', context)