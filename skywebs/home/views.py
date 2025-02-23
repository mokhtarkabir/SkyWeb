from django.shortcuts import render

# Create your views here.

def homePage(request):
    print("💛😂🤣this is the view of home app")
    return render(request, 'home/home.html')