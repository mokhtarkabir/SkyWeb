from django.shortcuts import render

# Create your views here.
def contactPage(request):
    return render(request, 'contact/contact.html')