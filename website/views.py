from django.contrib import messages
from django.shortcuts import render
from .forms import EnquiryForm, BookingForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    if request.method =='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            post.save()
            messages.success(request, 'Form submission successful')
    else:
        form = BookingForm()

    return render(request, 'website/index.html', {'form': form})

def contact(request):
    if request.method =='POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            post.save()
            messages.success(request, 'Form submission successful')
    else:
        form = EnquiryForm()

    return render(request, 'website/contact.html', {'form': form})

def services(request):
    return render(request, 'website/services.html')

def gallery(request):
    return render(request, 'website/gallery.html')
'''
def contact(request):
    form = EnquiryForm()
    return render(request, 'website/contact.html', {'form': form})
'''

def about(request):
    return render(request, 'website/about.html')
