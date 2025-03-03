from django.shortcuts import render
from .models import AboutPage, TeamMember
# Create your views here.

def aboutPage(request):
    aboutpage = AboutPage.objects.all()
    teamMember = TeamMember.objects.all()
    context ={
        'aboutpage': aboutpage,
        'teamMember':teamMember
    }
    return render(request, 'about/about.html', context)