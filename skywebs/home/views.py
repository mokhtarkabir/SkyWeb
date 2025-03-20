from django.shortcuts import render

from services.models import Service
from blog.models import Blog
from about.models import AboutPage, TeamMember
# Create your views here.

def homePage(request):
    services = Service.objects.all()[:3]
    aboutpage = AboutPage.objects.all()[:1]
    teamMember = TeamMember.objects.all()
    homeBlog = Blog.objects.all()[:3]
    context={
        'services': services,
        'aboutpage':aboutpage,
        'teamMember':teamMember,
        'blog':homeBlog
    }
    return render(request, 'home/home.html', context)