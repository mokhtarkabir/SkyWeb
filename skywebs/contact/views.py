from django.shortcuts import render, redirect
from .forms import ContactForm

def contactPage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.ip_address = request.META.get('REMOTE_ADDR')
            contact.save()
            return redirect('/')  # Create a success page
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})
