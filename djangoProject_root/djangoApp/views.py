from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

from .forms import ContactForm

def homepage(request):
    return render(request,"homepage.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanx , we recevid your message ')
        else:
            messages.warning(request, str(form.errors))        
    form = ContactForm()
    return render(request,"contactus.html",{'form':form})    