from email import message
from django import forms
from .models import Booking, Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        widgets={
            'name' :forms.TextInput(attrs={'class': 'form-group row form-control col-md-6 mb-4 mb-lg-0', 'placeholder': 'First And Last Name' }),
            'phone_number' :forms.TextInput(attrs={'class': 'form-group row col-md-6 form-control', 'placeholder': 'Phone Number'}),
            'email' :forms.TextInput(attrs={'class': 'form-group row col-md-12 form-control', 'placeholder': 'Email Address', 'col':'30', 'row':'10' }),
            'message' :forms.Textarea(attrs={'class' : 'form-group row col-md-12 form-control', 'placeholder': 'Write Your Message Here'}),
        }
        fields = ('name', 'phone_number', 'email', 'message')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'cf-1', 'placeholder': 'Your Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'cf-2', 'placeholder': 'Your Phone Number'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'cf-3', 'placeholder': 'Your Email Address'}),
            'wedding_date': forms.TextInput(attrs={'class': 'form-control datepicker px-3', 'id': 'cf-1', 'placeholder': 'Your Wedding Date'}),
            'wedding_colours': forms.TextInput(attrs={'class': 'form-control', 'id': 'cf-1', 'placeholder': 'Your Wedding Colours'}),
            'guests': forms.TextInput(attrs={'class': 'form-control', 'id': 'cf-1', 'placeholder': 'Number of Guests'}),
            'visit_date': forms.TextInput(attrs={'class': 'form-control datepicker px-3', 'id': 'cf-1', 'placeholder': 'Site Visit Date'}),
            'visit_time': forms.TextInput(attrs={'class': 'form-control', 'id': 'cf-1', 'placeholder': 'Time to Visit'}),
        }
        fields = ('name', 'phone_number', 'email', 'wedding_date', 'wedding_colours', 'guests', 'visit_date', 'visit_time',)
