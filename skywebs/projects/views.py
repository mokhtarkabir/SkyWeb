from django.shortcuts import render

# Create your views here.
# views.py
from .models import Projects

def projectsPage(request):
    templates = Projects.objects.all()
    return render(request, 'projects/projects.html', {'projects': templates})
