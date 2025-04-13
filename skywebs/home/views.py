from django.shortcuts import render

from services.models import Service
from blog.models import Blog
from about.models import AboutPage, TeamMember
from projects.models import Projects
from .models import CarouselSlide
# Create your views here.

def homePage(request):
    services = Service.objects.all()[:3]
    aboutpage = AboutPage.objects.all()[:1]
    teamMember = TeamMember.objects.all()
    homeBlog = Blog.objects.all()[:3]
    projects = Projects.objects.all()[:3]
    slideData = CarouselSlide.objects.all()
    context={
        'services': services,
        'aboutpage':aboutpage,
        'teamMember':teamMember,
        'blog':homeBlog,
        'projects':projects,
        'carouselData':slideData
    }
    return render(request, 'home/home.html', context)


