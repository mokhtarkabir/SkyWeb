from django.shortcuts import render

# Create your views here.

def projectsPage(request):
     return render(request, 'projects/projects.html')